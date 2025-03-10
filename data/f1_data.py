"""
class F1Data:
    @staticmethod
    def get_races():
        return [
            {
                'name': 'Bahrain Grand Prix',
                'date': '2024-03-02',
                'circuit': 'Bahrain International Circuit',
                'winner': 'Max Verstappen',
                'results': [
                    {'position': 1, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 25,
                     'time': '1:31:44.742'},
                    {'position': 2, 'driver': 'Sergio Perez', 'team': 'Red Bull Racing', 'points': 18,
                     'time': '+2.371s'},
                    {'position': 3, 'driver': 'Carlos Sainz', 'team': 'Ferrari', 'points': 15, 'time': '+8.645s'},
                    {'position': 4, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 12,
                     'time': '+11.987s'},
                    {'position': 5, 'driver': 'George Russell', 'team': 'Mercedes', 'points': 10,
                     'time': '+25.232s'},
                ]
            },
            {
                'name': 'Saudi Arabian Grand Prix',
                'date': '2024-03-09',
                'circuit': 'Jeddah Corniche Circuit',
                'winner': 'Max Verstappen',
                'results': [
                    {'position': 1, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 25,
                     'time': '1:29:23.227'},
                    {'position': 2, 'driver': 'Sergio Perez', 'team': 'Red Bull Racing', 'points': 18,
                     'time': '+13.643s'},
                    {'position': 3, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 15,
                     'time': '+18.639s'},
                    {'position': 4, 'driver': 'Oscar Piastri', 'team': 'McLaren', 'points': 12, 'time': '+32.183s'},
                    {'position': 5, 'driver': 'Fernando Alonso', 'team': 'Aston Martin', 'points': 10,
                     'time': '+35.866s'},
                ]
            },
            {
                'name': 'Australian Grand Prix',
                'date': '2024-03-24',
                'circuit': 'Albert Park Circuit',
                'winner': 'Carlos Sainz',
                'results': [
                    {'position': 1, 'driver': 'Carlos Sainz', 'team': 'Ferrari', 'points': 25,
                     'time': '1:30:33.122'},
                    {'position': 2, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 18,
                     'time': '+2.366s'},
                    {'position': 3, 'driver': 'Lando Norris', 'team': 'McLaren', 'points': 15, 'time': '+5.879s'},
                    {'position': 4, 'driver': 'Oscar Piastri', 'team': 'McLaren', 'points': 12, 'time': '+8.543s'},
                    {'position': 5, 'driver': 'Sergio Perez', 'team': 'Red Bull Racing', 'points': 10,
                     'time': '+14.166s'},
                ]
            },
            {
                'name': 'Japanese Grand Prix',
                'date': '2024-04-07',
                'circuit': 'Suzuka Circuit',
                'winner': 'Max Verstappen',
                'results': [
                    {'position': 1, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 25,
                     'time': '1:27:45.123'},
                    {'position': 2, 'driver': 'Sergio Perez', 'team': 'Red Bull Racing', 'points': 18,
                     'time': '+5.678s'},
                    {'position': 3, 'driver': 'Carlos Sainz', 'team': 'Ferrari', 'points': 15, 'time': '+12.345s'},
                    {'position': 4, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 12,
                     'time': '+15.789s'},
                    {'position': 5, 'driver': 'George Russell', 'team': 'Mercedes', 'points': 10,
                     'time': '+20.456s'},
                ]
            },
            {
                'name': 'Chinese Grand Prix',
                'date': '2024-04-21',
                'circuit': 'Shanghai International Circuit',
                'winner': 'Max Verstappen',
                'results': [
                    {'position': 1, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 25,
                     'time': '1:35:27.890'},
                    {'position': 2, 'driver': 'Lando Norris', 'team': 'McLaren', 'points': 18, 'time': '+3.456s'},
                    {'position': 3, 'driver': 'Sergio Perez', 'team': 'Red Bull Racing', 'points': 15,
                     'time': '+8.123s'},
                    {'position': 4, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 12,
                     'time': '+12.789s'},
                    {'position': 5, 'driver': 'George Russell', 'team': 'Mercedes', 'points': 10,
                     'time': '+15.456s'},
                ]
            },
            {
                'name': 'Miami Grand Prix',
                'date': '2024-05-05',
                'circuit': 'Miami International Autodrome',
                'winner': 'Lando Norris',
                'results': [
                    {'position': 1, 'driver': 'Lando Norris', 'team': 'McLaren', 'points': 25,
                     'time': '1:32:45.678'},
                    {'position': 2, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 18,
                     'time': '+2.345s'},
                    {'position': 3, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 15,
                     'time': '+5.678s'},
                    {'position': 4, 'driver': 'Carlos Sainz', 'team': 'Ferrari', 'points': 12, 'time': '+8.123s'},
                    {'position': 5, 'driver': 'George Russell', 'team': 'Mercedes', 'points': 10,
                     'time': '+10.456s'},
                ]
            },]

    @staticmethod
    def get_constructor_standings():
        return [
            {'position': 1, 'team': 'Red Bull Racing', 'points': 87, 'drivers': ['Max Verstappen', 'Sergio Perez']},
            {'position': 2, 'team': 'Ferrari', 'points': 49, 'drivers': ['Charles Leclerc', 'Carlos Sainz']},
            {'position': 3, 'team': 'McLaren', 'points': 28, 'drivers': ['Lando Norris', 'Oscar Piastri']},
            {'position': 4, 'team': 'Mercedes', 'points': 26, 'drivers': ['Lewis Hamilton', 'George Russell']},
            {'position': 5, 'team': 'Aston Martin', 'points': 19, 'drivers': ['Fernando Alonso', 'Lance Stroll']},
            {'position': 6, 'team': 'Alpine', 'points': 12, 'drivers': ['Pierre Gasly', 'Esteban Ocon']},
            {'position': 7, 'team': 'Williams', 'points': 8, 'drivers': ['Alexander Albon', 'Logan Sargeant']},
            {'position': 8, 'team': 'Alfa Romeo', 'points': 6, 'drivers': ['Valtteri Bottas', 'Zhou Guanyu']},
            {'position': 9, 'team': 'Haas F1 Team', 'points': 3, 'drivers': ['Nico Hulkenberg', 'Kevin Magnussen']},
            {'position': 10, 'team': 'AlphaTauri', 'points': 2, 'drivers': ['Yuki Tsunoda', 'Daniel Ricciardo']}
        ]

    @staticmethod
    def get_driver_standings():
        return [
            {'position': 1, 'name': 'Max Verstappen', 'points': 51, 'team': 'Red Bull Racing'},
            {'position': 2, 'name': 'Sergio Perez', 'points': 36, 'team': 'Red Bull Racing'},
            {'position': 3, 'name': 'Charles Leclerc', 'points': 28, 'team': 'Ferrari'},
            {'position': 4, 'name': 'Carlos Sainz', 'points': 21, 'team': 'Ferrari'},
            {'position': 5, 'name': 'Lando Norris', 'points': 18, 'team': 'McLaren'},
            {'position': 6, 'name': 'Lewis Hamilton', 'points': 16, 'team': 'Mercedes'},
            {'position': 7, 'name': 'Oscar Piastri', 'points': 10, 'team': 'McLaren'},
            {'position': 8, 'name': 'George Russell', 'points': 10, 'team': 'Mercedes'},
            {'position': 9, 'name': 'Fernando Alonso', 'points': 9, 'team': 'Aston Martin'},
            {'position': 10, 'name': 'Lance Stroll', 'points': 8, 'team': 'Aston Martin'},
            {'position': 11, 'name': 'Pierre Gasly', 'points': 6, 'team': 'Alpine'},
            {'position': 12, 'name': 'Alexander Albon', 'points': 4, 'team': 'Williams'},
            {'position': 13, 'name': 'Valtteri Bottas', 'points': 4, 'team': 'Alfa Romeo'},
            {'position': 14, 'name': 'Esteban Ocon', 'points': 4, 'team': 'Alpine'},
            {'position': 15, 'name': 'Nico Hulkenberg', 'points': 3, 'team': 'Haas F1 Team'},
            {'position': 16, 'name': 'Zhou Guanyu', 'points': 2, 'team': 'Alfa Romeo'},
            {'position': 17, 'name': 'Yuki Tsunoda', 'points': 2, 'team': 'AlphaTauri'},
            {'position': 18, 'name': 'Daniel Ricciardo', 'points': 0, 'team': 'AlphaTauri'},
            {'position': 19, 'name': 'Kevin Magnussen', 'points': 0, 'team': 'Haas F1 Team'},
            {'position': 20, 'name': 'Logan Sargeant', 'points': 0, 'team': 'Williams'}
        ]

    @staticmethod
    def get_drivers():
            return [
                {
                    'name': 'Lewis Hamilton',
                    'active_years': '2007-',
                    'teams': {
                        'McLaren': '2007-2012',
                        'Mercedes': '2013-'
                    },
                    'race_starts': 332,
                    'wins': 103,
                    'world_championships': 7
                },
                {
                    'name': 'Max Verstappen',
                    'active_years': '2015-',
                    'teams': {
                        'Toro Rosso': '2015-2016',
                        'Red Bull Racing': '2016-'
                    },
                    'race_starts': 188,
                    'wins': 54,
                    'world_championships': 3
                },
                {
                    'name': 'Sebastian Vettel',
                    'active_years': '2007-2022',
                    'teams': {
                        'BMW Sauber': '2007',
                        'Toro Rosso': '2007-2008',
                        'Red Bull Racing': '2009-2014',
                        'Ferrari': '2015-2020',
                        'Aston Martin': '2021-2022'
                    },
                    'race_starts': 299,
                    'wins': 53,
                    'world_championships': 4
                },
                {
                    'name': 'Fernando Alonso',
                    'active_years': '2001-',
                    'teams': {
                        'Minardi': '2001',
                        'Renault': '2003-2006, 2008-2009',
                        'McLaren': '2007, 2015-2018',
                        'Ferrari': '2010-2014',
                        'Aston Martin': '2023-'
                    },
                    'race_starts': 377,
                    'wins': 32,
                    'world_championships': 2
                }
            ]
"""

import pandas as pd


class F1Data:
    @staticmethod
    def load_data():
        """Charge les fichiers CSV nécessaires et les retourne sous forme de DataFrames."""
        drivers_df = pd.read_csv("data/drivers.csv")
        driver_standings_df = pd.read_csv("data/driver_standings.csv")
        races_df = pd.read_csv("data/races.csv")
        results_df = pd.read_csv("data/results.csv")
        return drivers_df, driver_standings_df, races_df, results_df

    @staticmethod
    def compute_wins(results_df, driver_id):
        """Calcule le nombre de victoires pour un pilote donné."""
        return results_df[(results_df['driverId'] == driver_id) & (results_df['positionOrder'] == 1)].shape[0]

    @staticmethod
    def compute_race_stats(driver_standings_df, races_df, driver_id):
        """Calcule le nombre de courses disputées et la période d'activité d'un pilote."""
        race_year_map = races_df.set_index('raceId')['year'].to_dict()
        driver_races = driver_standings_df[driver_standings_df['driverId'] == driver_id]

        if driver_races.empty:
            return 0, None

        race_ids = driver_races['raceId'].unique()
        years = [race_year_map[race_id] for race_id in race_ids if race_id in race_year_map]

        if years:
            return race_ids.size, f"{min(years)}-{max(years)}"
        else:
            return race_ids.size, None

    @staticmethod
    def get_data_drivers():
        """Retourne la liste des pilotes avec leurs statistiques calculées."""
        drivers_df, driver_standings_df, races_df, results_df = F1Data.load_data()
        drivers = drivers_df[['driverId', 'forename', 'surname']].to_dict(orient='records')

        for driver in drivers:
            driver_id = driver['driverId']
            driver['wins'] = F1Data.compute_wins(results_df, driver_id)
            driver['race_starts'], driver['active_years'] = F1Data.compute_race_stats(driver_standings_df, races_df,
                                                                                      driver_id)

            driver['world_championships'] = None  # Placeholder
            driver['teams'] = None  # Placeholder
            driver.pop('driverId', None)

        return drivers
    
    @staticmethod
    def get_races():
        return [
            {
                'name': 'Bahrain Grand Prix',
                'date': '2024-03-02',
                'circuit': 'Bahrain International Circuit',
                'winner': 'Max Verstappen',
                'results': [
                    {'position': 1, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 25,
                     'time': '1:31:44.742'},
                    {'position': 2, 'driver': 'Sergio Perez', 'team': 'Red Bull Racing', 'points': 18,
                     'time': '+2.371s'},
                    {'position': 3, 'driver': 'Carlos Sainz', 'team': 'Ferrari', 'points': 15, 'time': '+8.645s'},
                    {'position': 4, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 12,
                     'time': '+11.987s'},
                    {'position': 5, 'driver': 'George Russell', 'team': 'Mercedes', 'points': 10,
                     'time': '+25.232s'},
                ]
            },
            {
                'name': 'Saudi Arabian Grand Prix',
                'date': '2024-03-09',
                'circuit': 'Jeddah Corniche Circuit',
                'winner': 'Max Verstappen',
                'results': [
                    {'position': 1, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 25,
                     'time': '1:29:23.227'},
                    {'position': 2, 'driver': 'Sergio Perez', 'team': 'Red Bull Racing', 'points': 18,
                     'time': '+13.643s'},
                    {'position': 3, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 15,
                     'time': '+18.639s'},
                    {'position': 4, 'driver': 'Oscar Piastri', 'team': 'McLaren', 'points': 12, 'time': '+32.183s'},
                    {'position': 5, 'driver': 'Fernando Alonso', 'team': 'Aston Martin', 'points': 10,
                     'time': '+35.866s'},
                ]
            },
            {
                'name': 'Australian Grand Prix',
                'date': '2024-03-24',
                'circuit': 'Albert Park Circuit',
                'winner': 'Carlos Sainz',
                'results': [
                    {'position': 1, 'driver': 'Carlos Sainz', 'team': 'Ferrari', 'points': 25,
                     'time': '1:30:33.122'},
                    {'position': 2, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 18,
                     'time': '+2.366s'},
                    {'position': 3, 'driver': 'Lando Norris', 'team': 'McLaren', 'points': 15, 'time': '+5.879s'},
                    {'position': 4, 'driver': 'Oscar Piastri', 'team': 'McLaren', 'points': 12, 'time': '+8.543s'},
                    {'position': 5, 'driver': 'Sergio Perez', 'team': 'Red Bull Racing', 'points': 10,
                     'time': '+14.166s'},
                ]
            },
            {
                'name': 'Japanese Grand Prix',
                'date': '2024-04-07',
                'circuit': 'Suzuka Circuit',
                'winner': 'Max Verstappen',
                'results': [
                    {'position': 1, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 25,
                     'time': '1:27:45.123'},
                    {'position': 2, 'driver': 'Sergio Perez', 'team': 'Red Bull Racing', 'points': 18,
                     'time': '+5.678s'},
                    {'position': 3, 'driver': 'Carlos Sainz', 'team': 'Ferrari', 'points': 15, 'time': '+12.345s'},
                    {'position': 4, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 12,
                     'time': '+15.789s'},
                    {'position': 5, 'driver': 'George Russell', 'team': 'Mercedes', 'points': 10,
                     'time': '+20.456s'},
                ]
            },
            {
                'name': 'Chinese Grand Prix',
                'date': '2024-04-21',
                'circuit': 'Shanghai International Circuit',
                'winner': 'Max Verstappen',
                'results': [
                    {'position': 1, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 25,
                     'time': '1:35:27.890'},
                    {'position': 2, 'driver': 'Lando Norris', 'team': 'McLaren', 'points': 18, 'time': '+3.456s'},
                    {'position': 3, 'driver': 'Sergio Perez', 'team': 'Red Bull Racing', 'points': 15,
                     'time': '+8.123s'},
                    {'position': 4, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 12,
                     'time': '+12.789s'},
                    {'position': 5, 'driver': 'George Russell', 'team': 'Mercedes', 'points': 10,
                     'time': '+15.456s'},
                ]
            },
            {
                'name': 'Miami Grand Prix',
                'date': '2024-05-05',
                'circuit': 'Miami International Autodrome',
                'winner': 'Lando Norris',
                'results': [
                    {'position': 1, 'driver': 'Lando Norris', 'team': 'McLaren', 'points': 25,
                     'time': '1:32:45.678'},
                    {'position': 2, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 18,
                     'time': '+2.345s'},
                    {'position': 3, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 15,
                     'time': '+5.678s'},
                    {'position': 4, 'driver': 'Carlos Sainz', 'team': 'Ferrari', 'points': 12, 'time': '+8.123s'},
                    {'position': 5, 'driver': 'George Russell', 'team': 'Mercedes', 'points': 10,
                     'time': '+10.456s'},
                ]
            },]

    @staticmethod
    def get_constructor_standings():
        return [
            {'position': 1, 'team': 'Red Bull Racing', 'points': 87, 'drivers': ['Max Verstappen', 'Sergio Perez']},
            {'position': 2, 'team': 'Ferrari', 'points': 49, 'drivers': ['Charles Leclerc', 'Carlos Sainz']},
            {'position': 3, 'team': 'McLaren', 'points': 28, 'drivers': ['Lando Norris', 'Oscar Piastri']},
            {'position': 4, 'team': 'Mercedes', 'points': 26, 'drivers': ['Lewis Hamilton', 'George Russell']},
            {'position': 5, 'team': 'Aston Martin', 'points': 19, 'drivers': ['Fernando Alonso', 'Lance Stroll']},
            {'position': 6, 'team': 'Alpine', 'points': 12, 'drivers': ['Pierre Gasly', 'Esteban Ocon']},
            {'position': 7, 'team': 'Williams', 'points': 8, 'drivers': ['Alexander Albon', 'Logan Sargeant']},
            {'position': 8, 'team': 'Alfa Romeo', 'points': 6, 'drivers': ['Valtteri Bottas', 'Zhou Guanyu']},
            {'position': 9, 'team': 'Haas F1 Team', 'points': 3, 'drivers': ['Nico Hulkenberg', 'Kevin Magnussen']},
            {'position': 10, 'team': 'AlphaTauri', 'points': 2, 'drivers': ['Yuki Tsunoda', 'Daniel Ricciardo']}
        ]

    @staticmethod
    def get_driver_standings():
        return [
            {'position': 1, 'name': 'Max Verstappen', 'points': 51, 'team': 'Red Bull Racing'},
            {'position': 2, 'name': 'Sergio Perez', 'points': 36, 'team': 'Red Bull Racing'},
            {'position': 3, 'name': 'Charles Leclerc', 'points': 28, 'team': 'Ferrari'},
            {'position': 4, 'name': 'Carlos Sainz', 'points': 21, 'team': 'Ferrari'},
            {'position': 5, 'name': 'Lando Norris', 'points': 18, 'team': 'McLaren'},
            {'position': 6, 'name': 'Lewis Hamilton', 'points': 16, 'team': 'Mercedes'},
            {'position': 7, 'name': 'Oscar Piastri', 'points': 10, 'team': 'McLaren'},
            {'position': 8, 'name': 'George Russell', 'points': 10, 'team': 'Mercedes'},
            {'position': 9, 'name': 'Fernando Alonso', 'points': 9, 'team': 'Aston Martin'},
            {'position': 10, 'name': 'Lance Stroll', 'points': 8, 'team': 'Aston Martin'},
            {'position': 11, 'name': 'Pierre Gasly', 'points': 6, 'team': 'Alpine'},
            {'position': 12, 'name': 'Alexander Albon', 'points': 4, 'team': 'Williams'},
            {'position': 13, 'name': 'Valtteri Bottas', 'points': 4, 'team': 'Alfa Romeo'},
            {'position': 14, 'name': 'Esteban Ocon', 'points': 4, 'team': 'Alpine'},
            {'position': 15, 'name': 'Nico Hulkenberg', 'points': 3, 'team': 'Haas F1 Team'},
            {'position': 16, 'name': 'Zhou Guanyu', 'points': 2, 'team': 'Alfa Romeo'},
            {'position': 17, 'name': 'Yuki Tsunoda', 'points': 2, 'team': 'AlphaTauri'},
            {'position': 18, 'name': 'Daniel Ricciardo', 'points': 0, 'team': 'AlphaTauri'},
            {'position': 19, 'name': 'Kevin Magnussen', 'points': 0, 'team': 'Haas F1 Team'},
            {'position': 20, 'name': 'Logan Sargeant', 'points': 0, 'team': 'Williams'}
        ]
