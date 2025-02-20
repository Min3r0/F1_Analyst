from dash import Input, Output, State, callback, ctx, callback_context


def register_race_callbacks(app, races_data):
    @app.callback(
        [Output(f"modal-{race['name'].lower().replace(' ', '-')}", "is_open") for race in races_data],
        [Input(f"race-{race['name'].lower().replace(' ', '-')}", "n_clicks") for race in races_data] +
        [Input(f"close-{race['name'].lower().replace(' ', '-')}", "n_clicks") for race in races_data],
        prevent_initial_call=True
    )
    def toggle_modal(*args):
        triggered_id = ctx.triggered_id

        new_states = []
        for race in races_data:
            race_id = f"race-{race['name'].lower().replace(' ', '-')}"
            close_id = f"close-{race['name'].lower().replace(' ', '-')}"

            if triggered_id == race_id:
                new_states.append(True)
            elif triggered_id == close_id:
                new_states.append(False)
            else:
                new_states.append(False)

        return new_states


def register_standings_callbacks(app):
    @app.callback(
        Output("driver-standings-modal", "is_open"),
        [Input("driver-card", "n_clicks"),
         Input("close-driver-modal", "n_clicks")],
        prevent_initial_call=True
    )
    def toggle_driver_modal(open_clicks, close_clicks):
        triggered_id = ctx.triggered_id
        if triggered_id == "driver-card":
            return True
        return False

    @app.callback(
        Output("constructor-standings-modal", "is_open"),
        [Input("constructor-card", "n_clicks"),
         Input("close-constructor-modal", "n_clicks")],
        prevent_initial_call=True
    )
    def toggle_constructor_modal(open_clicks, close_clicks):
        triggered_id = ctx.triggered_id
        if triggered_id == "constructor-card":
            return True
        return False


@callback(
    Output("season-dropdown", "label"),
    [Input(f"season-{year}", "n_clicks") for year in range(2024, 1950, -1)],
    [State("season-dropdown", "label")]
)
def update_season(*args):
    ctx = callback_context
    if not ctx.triggered:
        return "SAISON"

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if button_id:
        year = button_id.split("-")[1]
        return f"SAISON {year}"

    return "SAISON"


@callback(
    [Output(f"season-{year}", "style") for year in range(2024, 1950, -1)],
    Input("season-search", "value")
)
def filter_seasons(search_term):
    if not search_term:
        return [{"display": "block"} for _ in range(2024, 1950, -1)]

    styles = []
    for year in range(2024, 1950, -1):
        if search_term.lower() in str(year):
            styles.append({"display": "block"})
        else:
            styles.append({"display": "none"})
    return styles