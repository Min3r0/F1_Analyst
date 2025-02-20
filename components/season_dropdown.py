from dash import html, dcc
import dash_bootstrap_components as dbc

def create_season_dropdown():
    seasons = list(range(2024, 1950, -1))
    
    return html.Div([
        dbc.DropdownMenu(
            [
                dbc.Input(
                    type="search",
                    placeholder="Rechercher une saison...",
                    className="mb-3",
                    id="season-search"
                ),
                html.Div([
                    dbc.DropdownMenuItem(
                        f"Saison {season}",
                        id=f"season-{season}"
                    ) for season in seasons
                ], style={"maxHeight": "300px", "overflowY": "auto"})
            ],
            label="SAISON",
            color="warning",
            id="season-dropdown"
        )
    ])