import pandas as pd
import numpy as np
import os
import json
import time
from concurrent.futures import ThreadPoolExecutor

class DataDrivers:
    _drivers_cache = None
    _cache_timestamp = 0
    _cache_duration = 3600
    _cache_file = "data/drivers_cache.json"

    @staticmethod
    def load_data():
        drivers_df = pd.read_csv("data/drivers.csv", usecols=['driverId', 'forename', 'surname'])
        driver_standings_df = pd.read_csv("data/driver_standings.csv", usecols=['driverId', 'raceId'])
        races_df = pd.read_csv("data/races.csv", usecols=['raceId', 'year'])
        results_df = pd.read_csv("data/results.csv", usecols=['driverId', 'raceId', 'constructorId', 'positionOrder', 'points'])
        constructors_df = pd.read_csv("data/constructors.csv", usecols=['constructorId', 'name'])
        return drivers_df, driver_standings_df, races_df, results_df, constructors_df

    @staticmethod
    def compute_driver_data(driver, driver_standings_df, races_df, results_df, constructors_df, race_year_map, constructor_map):
        driver_id = driver['driverId']
        driver_data = {'driverId': driver['driverId'],'forename': driver['forename'], 'surname': driver['surname'], 'wins':
            results_df[(results_df['driverId'] == driver_id) & (results_df['positionOrder'] == 1)].shape[0]}

        driver_races = driver_standings_df[driver_standings_df['driverId'] == driver_id]
        if driver_races.empty:
            driver_data['race_starts'], driver_data['active_years'] = 0, None
        else:
            race_ids = driver_races['raceId'].unique()
            years = [race_year_map[rid] for rid in race_ids if rid in race_year_map]
            if years:
                driver_data['race_starts'] = race_ids.size
                driver_data['active_years'] = f"{min(years)}-{max(years)}"
            else:
                driver_data['race_starts'], driver_data['active_years'] = race_ids.size, None

        temp_results = results_df.copy()
        temp_results['year'] = temp_results['raceId'].map(race_year_map)

        # Déterminer les champions du monde
        season_points = temp_results.groupby(['year', 'driverId'])['points'].sum().reset_index()
        champions = season_points.loc[season_points.groupby('year')['points'].idxmax()]
        driver_data['world_championships'] = (champions['driverId'] == driver_id).sum()

        # Extraire toutes les données de course du pilote
        temp_driver_results = temp_results[temp_results['driverId'] == driver_id]
        driver_data['total_points'] = temp_driver_results['points'].sum()
        # Ajout des positions du pilote (triées par année)
        positions = temp_driver_results.sort_values('year')['positionOrder'].tolist()
        driver_data['positions'] = positions

        # Construire les équipes + années
        driver_teams = temp_driver_results.groupby(['constructorId'])['year'].unique().to_dict()

        def format_years(years):
            years = sorted(years)
            ranges, start = [], years[0]
            for i in range(1, len(years)):
                if years[i] != years[i - 1] + 1:
                    ranges.append(f"{start}-{years[i - 1]}" if start != years[i - 1] else f"{start}")
                    start = years[i]
            ranges.append(f"{start}-{years[-1]}" if start != years[-1] else f"{start}")
            return " ".join(ranges)

        teams = {
            constructor_map[cid]: format_years(years)
            for cid, years in driver_teams.items() if cid in constructor_map
        }
        driver_data['teams'] = teams

        return driver_data

    @staticmethod
    def _save_cache(data):
        def convert_numpy_types(obj):
            if isinstance(obj, (np.integer,)):
                return int(obj)
            if isinstance(obj, (np.floating,)):
                return float(obj)
            raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

        os.makedirs(os.path.dirname(DataDrivers._cache_file), exist_ok=True)
        with open(DataDrivers._cache_file, 'w', encoding='utf-8') as f:
            json.dump({'timestamp': time.time(), 'data': data}, f, ensure_ascii=False, indent=2, default=convert_numpy_types)

    @staticmethod
    def _load_cache():
        if os.path.exists(DataDrivers._cache_file):
            try:
                with open(DataDrivers._cache_file, 'r', encoding='utf-8') as f:
                    cache = json.load(f)
                return cache['data'], cache['timestamp']
            except (json.JSONDecodeError, KeyError):
                return None, 0
        return None, 0

    @staticmethod
    def _is_cache_valid(timestamp):
        return time.time() - timestamp < DataDrivers._cache_duration

    @staticmethod
    def get_data_drivers():
        if DataDrivers._drivers_cache is not None and DataDrivers._is_cache_valid(DataDrivers._cache_timestamp):
            return DataDrivers._drivers_cache

        cache_data, cache_timestamp = DataDrivers._load_cache()
        if cache_data is not None and DataDrivers._is_cache_valid(cache_timestamp):
            DataDrivers._drivers_cache = cache_data
            DataDrivers._cache_timestamp = cache_timestamp
            return cache_data

        drivers_df, driver_standings_df, races_df, results_df, constructors_df = DataDrivers.load_data()
        race_year_map = races_df.set_index('raceId')['year'].to_dict()
        constructor_map = constructors_df.set_index('constructorId')['name'].to_dict()

        drivers = drivers_df.to_dict(orient='records')

        with ThreadPoolExecutor() as executor:
            results = executor.map(
                lambda d: DataDrivers.compute_driver_data(
                    d, driver_standings_df, races_df, results_df, constructors_df, race_year_map, constructor_map
                ),
                drivers
            )
            drivers_data = list(results)

        DataDrivers._drivers_cache = drivers_data
        DataDrivers._cache_timestamp = time.time()
        DataDrivers._save_cache(drivers_data)


        return drivers_data
