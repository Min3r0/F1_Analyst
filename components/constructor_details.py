from dash import html, dcc
import plotly.express as px


def get_constructor_details(constructor):
    if not constructor:
        return html.Div("Aucun constructeur sélectionné.")

    season_positions = constructor.get('season_positions', {})

    # Si pas de données de position, message seulement
    if not season_positions:
        return html.Div([
            html.H4(constructor['name']),
            html.P(f"Nationalité : {constructor.get('nationality', 'Inconnu')}"),
            html.P(f"Années d'existence : {constructor.get('existence_years', 'Inconnu')}"),
            html.H5("Pilotes ayant couru pour cette écurie :"),
            html.Ul([html.Li(f"{driver} ({years})") for driver, years in constructor.get('drivers', {}).items()]) or html.P("Aucun pilote listé"),
            html.P("Aucune donnée de position en championnat disponible pour ce constructeur.")
        ])

    years = sorted(season_positions.keys())
    positions = [season_positions[y] for y in years]

    fig = px.bar(
        x=years,
        y=positions,
        labels={"x": "Saison", "y": "Position"},
        title=f"Meilleure position en championnat par saison - {constructor['name']}",
        text=positions,
        range_y=[max(positions)+1, 1]  # Inverser axe y
    )

    drivers_list = [f"{driver} ({years})" for driver, years in constructor.get('drivers', {}).items()]

    return html.Div([
        html.H4(constructor['name']),
        html.P(f"Nationalité : {constructor.get('nationality', 'Inconnu')}"),
        html.P(f"Années d'existence : {constructor.get('existence_years', 'Inconnu')}"),
        html.H5("Pilotes ayant couru pour cette écurie :"),
        html.Ul([html.Li(d) for d in drivers_list]) if drivers_list else html.P("Aucun pilote listé"),
        dcc.Graph(figure=fig)
    ])
