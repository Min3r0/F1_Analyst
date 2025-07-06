import pandas as pd
import os

def get_data_circuits():
    # Chemin vers le fichier circuits.csv
    path = os.path.join("data", "circuits.csv")
    df = pd.read_csv(path)

    # On sélectionne et renomme les colonnes importantes
    df = df[["circuitId", "name", "location", "country"]]
    df["name"] = df["name"].str.strip()

    # On convertit en dictionnaires
    circuits = df.to_dict("records")
    return circuits
