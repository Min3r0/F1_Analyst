# season_layout.py
from dash import html
import dash_bootstrap_components as dbc
from components.modals.race_modal import create_race_modal
from components.modals.standings_modal import create_driver_standings_modal, create_constructor_standings_modal
from components.standings_cards import create_constructor_card, create_driver_card
from components.race_card import create_race_card
from data.f1_data import F1Data


def create_season_content():
    # Get data
    races = F1Data.get_races()
    constructor_standings = F1Data.get_constructor_standings()
    driver_standings = F1Data.get_driver_standings()

    return html.Div([
        # Standings Section
        html.Div([
            html.Div([
                create_constructor_card(constructor_standings)
            ], className="col-6"),
            html.Div([
                create_driver_card(driver_standings)
            ], className="col-6")
        ], className="row g-4 mb-4"),

        # Races Grid
        html.Div([
            html.Div([
                create_race_card(race)
            ], className="col-6 mb-4")
            for race in races
        ], className="row"),

        # Modales
        html.Div([
            create_race_modal(race) for race in races
        ]),
        create_driver_standings_modal(driver_standings),
        create_constructor_standings_modal(constructor_standings)
    ])