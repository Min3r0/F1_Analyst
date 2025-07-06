from dash import html, dcc
import plotly.express as px

def get_driver_details(driver):
    if not driver:
        return html.Div("Aucun pilote sélectionné.")

    # Initialiser toutes les positions de 1 à 20 à 0
    positions_count = {str(i): 0 for i in range(1, 21)}
    positions_count["21+"] = 0

    # Compter les positions (avec regroupement au-delà de 20)
    for pos in driver['positions']:
        if pos > 20:
            positions_count["21+"] += 1
        else:
            positions_count[str(pos)] += 1

    sorted_keys = [str(i) for i in range(1, 21)] + ["21+"]

    # Graphique en barres : nombre de fois par position
    bar_fig = px.bar(
        x=sorted_keys,
        y=[positions_count[k] for k in sorted_keys],
        labels={"x": "Position", "y": "Nombre de fois"},
        title="Nombre de fois par position",
    )

    total_courses = len(driver['positions'])
    wins = driver.get('wins', 0)
    podiums = sum(positions_count.get(pos, 0) for pos in ['1', '2', '3'])

    # Diagramme donut Victoires vs Autres courses
    pie_wins = px.pie(
        names=['Victoires', 'Autres courses'],
        values=[wins, max(total_courses - wins, 0)],
        title="Victoires sur total des courses",
        hole=0.5  # Trou au milieu pour faire un anneau
    )

    # Diagramme donut Podiums vs autres courses
    pie_podiums = px.pie(
        names=['Podiums (1, 2, 3)', 'Autres courses'],
        values=[podiums, max(total_courses - podiums, 0)],
        title="Podiums (1-2-3) sur total des courses",
        hole=0.5
    )

    return html.Div([
        html.H4(f"{driver['forename']} {driver['surname']}"),
        html.P(f"Débuts en F1 : {driver.get('active_years', 'Inconnu')}"),
        html.P(f"Nombre de victoires : {wins}"),
        html.P(f"Titres mondiaux : {driver['world_championships']}"),
        html.P(f"Équipes : {', '.join([f'{k} ({v})' for k, v in driver['teams'].items()])}"),
        html.P(f"Total de points : {driver.get('total_points', 0)}"),

        html.H5("Nombre de fois par position :"),
        dcc.Graph(figure=bar_fig),

        html.Div([
            dcc.Graph(figure=pie_wins, style={"display": "inline-block", "width": "49%"}),
            dcc.Graph(figure=pie_podiums, style={"display": "inline-block", "width": "49%"}),
        ], style={"display": "flex", "justifyContent": "space-between"})
    ])
