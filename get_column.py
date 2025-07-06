import pandas as pd
import os


def get_csv_columns(file_paths):
    columns_dict = {}

    for path in file_paths:
        try:
            df = pd.read_csv(path, nrows=0)
            columns_dict[os.path.basename(path)] = list(df.columns)
        except Exception as e:
            columns_dict[os.path.basename(path)] = f"Erreur : {e}"

    return columns_dict


if __name__ == "__main__":
    fichiers_csv = [
        "C:/Users/romai/Documents/B3/FF11/data/constructor_results.csv",
        "C:/Users/romai/Documents/B3/FF11/data/constructors.csv",
        "C:/Users/romai/Documents/B3/FF11/data/constructor_standings.csv",
        "C:/Users/romai/Documents/B3/FF11/data/results.csv",
        "C:/Users/romai/Documents/B3/FF11/data/drivers.csv",
        "C:/Users/romai/Documents/B3/FF11/data/circuits.csv",
        "C:/Users/romai/Documents/B3/FF11/data/driver_standings.csv",
        "C:/Users/romai/Documents/B3/FF11/data/lap_times.csv",
        "C:/Users/romai/Documents/B3/FF11/data/pit_stop.csv",
        "C:/Users/romai/Documents/B3/FF11/data/qualifying.csv",
        "C:/Users/romai/Documents/B3/FF11/data/races.csv",
        "C:/Users/romai/Documents/B3/FF11/data/seasons.csv",
        "C:/Users/romai/Documents/B3/FF11/data/sprint_results.csv",
        "C:/Users/romai/Documents/B3/FF11/data/status.csv"
    ]

    colonnes = get_csv_columns(fichiers_csv)

    for fichier, cols in colonnes.items():
        print(f"{fichier} : {cols}")
