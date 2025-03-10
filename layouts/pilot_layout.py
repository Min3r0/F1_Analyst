# pilot_layout.py
from dash import html
from data.f1_data import F1Data


def create_pilot_card(driver):
    return html.Div([
        html.Div([
            html.Div([
                html.H3(driver['forename'] + " " + driver['surname'], className="mb-0 fw-bold text-white"),
                html.P([
                    "Active years: ",
                    html.Span(driver['active_years'], className="text-warning")
                ], className="mb-2 text-white"),
                html.Hr(className="border-danger opacity-25"),
                html.Div([
                    html.P([
                        html.Span("Race starts: ", className="text-muted"),
                        html.Span(str(driver['race_starts']), className="text-warning")
                    ], className="mb-1"),
                    html.P([
                        html.Span("Wins: ", className="text-muted"),
                        html.Span(str(driver['wins']), className="text-warning")
                    ], className="mb-1"),
                    html.P([
                        html.Span("World Championships: ", className="text-muted"),
                        html.Span(str(driver['world_championships']), className="text-warning")
                    ], className="mb-3")
                ]),
                html.Hr(className="border-danger opacity-25"),
                html.Div([
                    html.H6("Teams:", className="text-muted mb-2"),
                    html.Div([
                        html.Div([
                            html.Span(team + ": ", className="text-muted"),
                            html.Span(years, className="text-warning")
                        ], className="mb-1")
                        for team, years in driver['teams'].items()
                    ])
                ])
            ], className="p-4")
        ], className="card h-100 bg-dark border border-danger")
    ], className="col-6 mb-4")


def create_pilot_content():
    # Get drivers data
    drivers = F1Data.get_data_drivers()

    return html.Div([
        # Drivers Grid
        html.Div([
            create_pilot_card(driver)
            for driver in drivers
        ], className="row")
    ])