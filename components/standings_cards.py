from dash import html
import dash_bootstrap_components as dbc

def create_constructor_card(constructor_standings):
    return html.Div(
        dbc.Card([
            dbc.CardBody([
                html.Div([
                    html.I(className="bi bi-people-fill text-danger me-2"),
                    html.H5("Classement Constructeurs", className="mb-0 fw-bold")
                ], className="d-flex align-items-center mb-4"),
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Span(f"{team['position']}", className="text-warning fw-bold me-2"),
                                html.Span(team['team'], className="fw-medium")
                            ], className="d-flex align-items-center"),
                            html.Span(f"{team['points']} pts", className="text-warning")
                        ], className="d-flex justify-content-between align-items-center mb-2"),
                        html.Div([
                            html.Div(driver, className="text-muted small")
                            for driver in team['drivers']
                        ], className="ms-4")
                    ], className="border-bottom border-secondary pb-3 mb-3")
                    for team in constructor_standings[:3]
                ])
            ])
        ], className="h-100 bg-dark text-white border-danger"),
        id="constructor-card",
        n_clicks=0,
        style={"cursor": "pointer"}
    )

def create_driver_card(driver_standings):
    return html.Div(
        dbc.Card([
            dbc.CardBody([
                html.Div([
                    html.I(className="bi bi-trophy-fill text-danger me-2"),
                    html.H5("Classement Pilotes", className="mb-0 fw-bold")
                ], className="d-flex align-items-center mb-4"),
                html.Div([
                    html.Div([
                        html.Div([
                            html.Span(f"{driver['position']}", className="text-warning fw-bold me-2"),
                            html.Span(driver['name'], className="fw-medium")
                        ], className="d-flex align-items-center"),
                        html.Span(f"{driver['points']} pts", className="text-warning")
                    ], className="d-flex justify-content-between align-items-center border-bottom border-secondary pb-3 mb-3")
                    for driver in driver_standings[:5]
                ])
            ])
        ], className="h-100 bg-dark text-white border-danger"),
        id="driver-card",
        n_clicks=0,
        style={"cursor": "pointer"}
    )