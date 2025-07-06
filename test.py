import pandas as pd
import json

# Chargement des données
results = pd.read_csv('data/results.csv')
races = pd.read_csv('data/races.csv')
constructors = pd.read_csv('data/constructors.csv')
drivers = pd.read_csv('data/drivers.csv')
status = pd.read_csv('data/status.csv')
qualifying = pd.read_csv('data/qualifying.csv')

# Fusion résultats + courses pour avoir les années
results = results.merge(races[['raceId', 'year']], on='raceId')

# Choisir l'année à construire
target_year = 2024

year_results = results[results['year'] == target_year]

# Création du JSON final
constructor_data = []

for constructor_id, group in year_results.groupby('constructorId'):
    constructor_name = constructors.loc[constructors['constructorId'] == constructor_id, 'name'].values[0]

    total_points = group['points'].sum()
    wins = group[group['positionOrder'] == 1].shape[0]
    avg_finish = group['positionOrder'].replace(0, pd.NA).dropna().astype(int).mean()
    dnf_count = group[group['statusId'].isin(status[status['status'].str.contains("Retired|Accident|Engine", na=False)]['statusId'])].shape[0]

    # Qualifying moyenne
    group_qual = qualifying[(qualifying['raceId'].isin(group['raceId'])) & (qualifying['constructorId'] == constructor_id)]
    avg_qual_pos = group_qual['position'].replace(0, pd.NA).dropna().mean()

    # Pilotes
    pilot_data = []
    for driver_id, driver_group in group.groupby('driverId'):
        driver_info = drivers[drivers['driverId'] == driver_id].iloc[0]
        pilot_data.append({
            'driver_id': int(driver_id),
            'name': f"{driver_info['forename']} {driver_info['surname']}",
            'points': driver_group['points'].sum(),
            'avg_grid': driver_group['grid'].replace(0, pd.NA).dropna().mean(),
            'avg_finish': driver_group['positionOrder'].replace(0, pd.NA).dropna().astype(int).mean(),
            'wins': driver_group[driver_group['positionOrder'] == 1].shape[0],
            'dnf': driver_group[driver_group['statusId'].isin(status[status['status'].str.contains("Retired|Accident|Engine", na=False)]['statusId'])].shape[0]
        })

    constructor_data.append({
        'year': target_year,
        'constructor': constructor_name,
        'constructor_id': int(constructor_id),
        'total_points': float(total_points),
        'wins': int(wins),
        'avg_qualifying_pos': float(avg_qual_pos) if pd.notna(avg_qual_pos) else None,
        'avg_finish_pos': float(avg_finish) if pd.notna(avg_finish) else None,
        'dnf_count': int(dnf_count),
        'pilots': pilot_data
    })

# Sauvegarde du JSON
with open(f'data/constructor_summary_{target_year}.json', 'w') as f:
    json.dump(constructor_data, f, indent=2)
