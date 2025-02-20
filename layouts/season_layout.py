from dash import html
import dash_bootstrap_components as dbc

from components.modals.race_modal import create_race_modal
from components.modals.standings_modal import create_driver_standings_modal, create_constructor_standings_modal
from components.season_dropdown import create_season_dropdown
from components.standings_cards import create_constructor_card, create_driver_card
from components.race_card import create_race_card
from data.f1_data import F1Data


def create_season_layout():
    # Get data
    races = F1Data.get_races()
    constructor_standings = F1Data.get_constructor_standings()
    driver_standings = F1Data.get_driver_standings()

    # Create layout
    return html.Div([
        # Header
        html.Header([
            html.Div([
                html.I(className="bi bi-flag-fill text-danger fs-4 me-2"),
                html.H1("F1 PREDICTIONS", className="mb-0 fw-bold")
            ], className="d-flex align-items-center"),

            html.Nav([
                create_season_dropdown(),
                html.Button("PILOTE", className="btn btn-link text-muted text-decoration-none"),
                html.Button("CONSTRUCTEUR", className="btn btn-link text-muted text-decoration-none"),
                html.Button("CIRCUIT", className="btn btn-link text-muted text-decoration-none")
            ], className="d-flex gap-4 align-items-center")
        ], className="d-flex justify-content-between align-items-center mb-4"),

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

    ], className="container-fluid bg-black text-white p-4")