from dash import html
import dash_bootstrap_components as dbc

def create_driver_standings_modal(driver_standings):
    return dbc.Modal(
        [
            dbc.ModalHeader("Classement Pilotes"),
            dbc.ModalBody([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Span(f"{driver['position']}", className="text-warning fw-bold me-3 w-8"),
                            html.Div([
                                html.Div(driver['name'], className="fw-medium"),
                                html.Div(driver['team'], className="text-muted small")
                            ])
                        ], className="d-flex align-items-center"),
                        html.Span(f"{driver['points']} pts", className="text-warning fw-bold")
                    ], className="d-flex justify-content-between align-items-center border-bottom border-secondary pb-3 mb-3")
                    for driver in driver_standings
                ])
            ]),
            dbc.ModalFooter(
                dbc.Button("Fermer", id="close-driver-modal", className="ml-auto", n_clicks=0)
            ),
        ],
        id="driver-standings-modal",
        is_open=False,
        size="lg"
    )

def create_constructor_standings_modal(constructor_standings):
    return dbc.Modal(
        [
            dbc.ModalHeader("Classement Constructeurs"),
            dbc.ModalBody([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Span(f"{team['position']}", className="text-warning fw-bold me-3"),
                                html.Span(team['team'], className="fw-medium fs-5")
                            ], className="d-flex align-items-center"),
                            html.Span(f"{team['points']} pts", className="text-warning fw-bold")
                        ], className="d-flex justify-content-between align-items-center mb-2"),
                        html.Div([
                            html.Div(driver, className="text-muted")
                            for driver in team['drivers']
                        ], className="ms-4 row row-cols-2")
                    ], className="border-bottom border-secondary pb-4 mb-4")
                    for team in constructor_standings
                ])
            ]),
            dbc.ModalFooter(
                dbc.Button("Fermer", id="close-constructor-modal", className="ml-auto", n_clicks=0)
            ),
        ],
        id="constructor-standings-modal",
        is_open=False,
        size="lg"
    )