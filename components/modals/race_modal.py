from dash import html
import dash_bootstrap_components as dbc

def create_race_modal(race_data):
    return dbc.Modal(
        [
            dbc.ModalHeader(f"Résultats de la course - {race_data['name']}"),
            dbc.ModalBody([
                html.Div([
                    html.P(f"Circuit: {race_data['circuit']}", className="fw-medium"),
                    html.P(f"Date: {race_data['date']}", className="fw-medium"),
                    html.P(f"Winner: {race_data['winner']}", className="fw-medium text-warning"),
                    html.Div(
                        "Course à venir" if not race_data.get('results') else [
                            html.Div([
                                html.Div([
                                    html.Span(f"{result['position']}", className="text-warning fw-bold me-3"),
                                    html.Div([
                                        html.Div(result['driver'], className="fw-medium"),
                                        html.Div(result['team'], className="text-muted small")
                                    ])
                                ], className="d-flex align-items-center"),
                                html.Div([
                                    html.Div(f"{result['points']} pts", className="text-warning fw-bold"),
                                    html.Div(result.get('time', ''), className="text-muted small")
                                ], className="text-end")
                            ], className="d-flex justify-content-between align-items-center border-bottom border-secondary pb-3 mb-3")
                            for result in race_data.get('results', [])
                        ],
                        className="mt-4"
                    )
                ])
            ]),
            dbc.ModalFooter(
                dbc.Button(
                    "Fermer",
                    id=f"close-{race_data['name'].lower().replace(' ', '-')}",
                    className="ml-auto",
                    n_clicks=0
                )
            ),
        ],
        id=f"modal-{race_data['name'].lower().replace(' ', '-')}",
        is_open=False,
        size="lg"
    )