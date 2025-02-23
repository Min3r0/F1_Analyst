from dash import html, dcc
from components.season_dropdown import create_season_dropdown


def create_header():
    return html.Header([
        html.Div([
            html.I(className="bi bi-flag-fill text-danger fs-4 me-2"),
            html.H1("F1 PREDICTIONS", className="mb-0 fw-bold")
        ], className="d-flex align-items-center"),

        html.Nav([
            create_season_dropdown(),
            html.Button("PILOTE", id='btn-pilot', className="btn btn-link text-muted text-decoration-none"),
            html.Button("CONSTRUCTEUR", className="btn btn-link text-muted text-decoration-none"),
            html.Button("CIRCUIT", className="btn btn-link text-muted text-decoration-none")
        ], className="d-flex gap-4 align-items-center")
    ], className="d-flex justify-content-between align-items-center mb-4")


def create_main_layout():
    from layouts.season_layout import create_season_content

    return html.Div([
        # Hidden URL component for navigation
        dcc.Location(id='url', refresh=False),

        # Common header
        create_header(),

        # Content div that will be updated
        html.Div(id='page-content', children=create_season_content())
    ], className="container-fluid bg-black text-white p-4")