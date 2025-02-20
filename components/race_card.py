from dash import html
import dash_bootstrap_components as dbc

def create_race_card(race):
    return html.Div(
        dbc.Card([
            dbc.CardBody([
                html.Div([
                    html.H5(race['name'], className="mb-0 fw-bold"),
                    html.Div([
                        html.I(className="bi bi-clock me-2"),
                        html.Span(race['date'])
                    ], className="text-muted d-flex align-items-center")
                ], className="d-flex justify-content-between align-items-center mb-4"),
                html.Div([
                    html.Div([
                        html.P("Circuit", className="text-muted mb-1"),
                        html.P(race['circuit'], className="fw-medium")
                    ], className="col"),
                    html.Div([
                        html.P("Prédiction", className="text-muted mb-1"),
                        html.P(race['winner'], className="fw-medium text-warning")
                    ], className="col")
                ], className="row")
            ])
        ], className="bg-dark text-white border-danger h-100"),
        id=f"race-{race['name'].lower().replace(' ', '-')}",
        n_clicks=0,
        style={"cursor": "pointer"}
    )