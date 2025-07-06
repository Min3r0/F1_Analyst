import pandas as pd
import os
import json
import time
from concurrent.futures import ThreadPoolExecutor


class DataConstructors:
    _cache_file = "data/constructors_cache.json"
    _cache_duration = 3600
    _cache = None
    _timestamp = 0

    @staticmethod
    def load_data():
        constructors_df = pd.read_csv("data/constructors.csv", usecols=['constructorId', 'name', 'nationality'])
        results_df = pd.read_csv("data/results.csv", usecols=['constructorId', 'driverId', 'raceId'])
        constructor_standings_df = pd.read_csv("data/constructor_standings.csv", usecols=['constructorId', 'raceId', 'position'])
        races_df = pd.read_csv("data/races.csv", usecols=['raceId', 'year'])
        drivers_df = pd.read_csv("data/drivers.csv", usecols=['driverId', 'forename', 'surname'])
        return constructors_df, results_df, constructor_standings_df, races_df, drivers_df

    @staticmethod
    def compute_constructor_data(constructor, results_df, standings_df, races_df, drivers_df, race_year_map):
        constructor_id = constructor['constructorId']
        constructor_data = {
            'constructorId': constructor_id,
            'name': constructor['name'],
            'nationality': constructor['nationality'],
        }

        # Récupérer les courses de cette écurie
        constructor_races = results_df[results_df['constructorId'] == constructor_id]
        if constructor_races.empty:
            constructor_data['existence_years'] = None
        else:
            race_ids = constructor_races['raceId'].unique()
            years = [race_year_map[rid] for rid in race_ids if rid in race_year_map]
            if years:
                constructor_data['existence_years'] = f"{min(years)}-{max(years)}"
            else:
                constructor_data['existence_years'] = None

        # Pilotes ayant couru pour cette écurie
        pilot_links = constructor_races[['driverId', 'raceId']]
        pilot_links['year'] = pilot_links['raceId'].map(race_year_map)

        pilot_years = pilot_links.groupby('driverId')['year'].apply(list).to_dict()

        drivers_map = drivers_df.set_index('driverId').apply(lambda x: f"{x['forename']} {x['surname']}", axis=1).to_dict()

        def format_years(years):
            years = sorted(set(years))
            ranges, start = [], years[0]
            for i in range(1, len(years)):
                if years[i] != years[i - 1] + 1:
                    ranges.append(f"{start}-{years[i - 1]}" if start != years[i - 1] else f"{start}")
                    start = years[i]
            ranges.append(f"{start}-{years[-1]}" if start != years[-1] else f"{start}")
            return " ".join(ranges)

        constructor_data['drivers'] = {
            drivers_map[did]: format_years(years)
            for did, years in pilot_years.items() if did in drivers_map
        }

        # Position finale par saison
        standings = standings_df[standings_df['constructorId'] == constructor_id].copy()
        standings['year'] = standings['raceId'].map(race_year_map)
        standings = standings.dropna(subset=['year', 'position'])

        season_positions = standings.groupby('year')['position'].min().to_dict()
        constructor_data['season_positions'] = {
            int(year): int(pos) for year, pos in season_positions.items()
        }

        return constructor_data

    @staticmethod
    def _is_cache_valid():
        return time.time() - DataConstructors._timestamp < DataConstructors._cache_duration

    @staticmethod
    def _load_cache():
        if os.path.exists(DataConstructors._cache_file):
            try:
                with open(DataConstructors._cache_file, 'r', encoding='utf-8') as f:
                    cache = json.load(f)
                return cache['data'], cache['timestamp']
            except Exception:
                return None, 0
        return None, 0

    @staticmethod
    def _save_cache(data):
        os.makedirs(os.path.dirname(DataConstructors._cache_file), exist_ok=True)
        with open(DataConstructors._cache_file, 'w', encoding='utf-8') as f:
            json.dump({'data': data, 'timestamp': time.time()}, f, indent=2)

    @staticmethod
    def get_data_constructors():
        if DataConstructors._cache and DataConstructors._is_cache_valid():
            return DataConstructors._cache

        cache_data, timestamp = DataConstructors._load_cache()
        if cache_data and (time.time() - timestamp < DataConstructors._cache_duration):
            DataConstructors._cache = cache_data
            DataConstructors._timestamp = timestamp
            return cache_data

        constructors_df, results_df, standings_df, races_df, drivers_df = DataConstructors.load_data()
        race_year_map = races_df.set_index('raceId')['year'].to_dict()

        constructors = constructors_df.to_dict(orient='records')

        with ThreadPoolExecutor() as executor:
            results = executor.map(
                lambda c: DataConstructors.compute_constructor_data(
                    c, results_df, standings_df, races_df, drivers_df, race_year_map
                ),
                constructors
            )
            constructor_data = list(results)

        DataConstructors._cache = constructor_data
        DataConstructors._timestamp = time.time()
        DataConstructors._save_cache(constructor_data)

        return constructor_data
