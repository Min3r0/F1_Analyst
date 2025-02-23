from dash import Input, Output


def register_navigation_callbacks(app):
    @app.callback(
        Output('url', 'pathname'),
        Input('btn-pilot', 'n_clicks'),
        prevent_initial_call=True
    )
    def navigate_to_pilot(n_clicks):
        if n_clicks:
            return '/pilot'
        return '/'

    @app.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname')
    )
    def display_page(pathname):
        from layouts.pilot_layout import create_pilot_content
        from layouts.season_layout import create_season_content

        if pathname == '/pilot':
            return create_pilot_content()
        return create_season_content()