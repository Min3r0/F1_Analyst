# components/prediction_detail.py
import pandas as pd
from dash import dash_table


def get_prediction_details():
    # Importer les résultats depuis un CSV ou exécuter le code de prédiction ici
    results_df = pd.read_csv("data/predictions_summary.csv")  # Préparé à l'avance

    return dash_table.DataTable(
        data=results_df.to_dict("records"),
        columns=[{"name": col, "id": col} for col in results_df.columns],
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'center', 'padding': '5px'},
        style_header={'backgroundColor': 'black', 'color': 'white'},
        style_data={'backgroundColor': '#1a1a1a', 'color': 'white'},
    )
