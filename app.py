from dash import Dash, html, dcc, Input, Output, State, callback_context, ALL, dash
from dash.dependencies import MATCH
import dash_bootstrap_components as dbc
from utils.data_drivers import DataDrivers
from utils.data_constructors import DataConstructors
from components.driver_details import get_driver_details
from components.constructor_details import get_constructor_details
from components.prediction_details import get_prediction_details
from components.circuit_details import get_data_circuits
from prediction_1 import confusion_images, predicted_2024



app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server



# Données pilotes et constructeurs
drivers = DataDrivers.get_data_drivers()
drivers_sorted = sorted(drivers, key=lambda d: (d['surname'], d['forename']))
constructors = DataConstructors.get_data_constructors()
constructors_sorted = sorted(constructors, key=lambda c: c['name'])

# Pour suggestions circuits
circuits = get_data_circuits()
circuits_sorted = sorted(circuits, key=lambda c: c['name'])

# Stockage temporaire pour Prediction V2
selected_teams = []
selected_circuits = []


# Layout avec navigation simple par onglets
app.layout = html.Div([


    dbc.Tabs([
        dbc.Tab(label="Pilotes", tab_id="tab-drivers"),
        dbc.Tab(label="Constructeurs", tab_id="tab-constructors"),
        dbc.Tab(label="Predictions", tab_id="tab-predictions"),
        dbc.Tab(label="Prediction_V2", tab_id="tab-predictions-V2"),
    ], id="tabs", active_tab="tab-drivers"),

    html.Div(id="page-content", style={"padding": "10px"})
])

# Callback pour afficher la page active
@app.callback(
    Output("page-content", "children"),
    Input("tabs", "active_tab")
)
def render_tab_content(active_tab):
    if active_tab == "tab-drivers":
        return html.Div([
            html.Div([
                html.H4("Liste des pilotes"),
                dcc.Input(id="search-bar", type="text", placeholder="Rechercher...", debounce=True),
                html.Div(id="driver-list", className="driver-list")
            ], style={"width": "25%", "display": "inline-block", "verticalAlign": "top"}),

            html.Div([
                html.H3("Détails du pilote"),
                html.Div(id="driver-details")
            ], style={"width": "74%", "display": "inline-block", "padding": "10px"})
        ])


    elif active_tab == "tab-constructors":
        return html.Div([
            html.Div([
                html.H4("Liste des constructeurs"),
                dcc.Input(id="search-bar-constructors", type="text", placeholder="Rechercher...", debounce=True),
                html.Div(id="constructor-list", className="constructor-list")
            ], style={"width": "25%", "display": "inline-block", "verticalAlign": "top"}),
            html.Div([
                html.H3("Détails du constructeur"),
                html.Div(id="constructor-details")
            ], style={"width": "74%", "display": "inline-block", "padding": "10px"})
        ])




    elif active_tab == "tab-predictions":

        return html.Div([

            html.H3("Prédictions de champion constructeur"),

            html.P("Comparaison saison par saison (modèles : Random Forest, Logistic Regression, etc.)"),

            get_prediction_details(),

            html.Hr(),

            html.H4("Prédiction du championnat 2024 par modèle :"),

            html.Div([

                html.Div([

                    html.H5(model_name),

                    html.Ol([html.Li(team) for team in team_ranking])

                ], style={"marginBottom": "20px"})

                for model_name, team_ranking in predicted_2024.items()

            ]),

            html.Hr(),
            html.H4("Matrices de confusion des modèles :"),
            html.Div([
                html.Div([
                    html.H5(model_name),
                    html.Img(src=img_src, style={"width": "400px", "margin": "10px", "border": "1px solid #444"})
                ], style={"display": "inline-block", "textAlign": "center", "marginRight": "20px"})
                for model_name, img_src in confusion_images.items()
            ], style={"display": "flex", "flexWrap": "wrap"})
        ])

    elif active_tab == "tab-predictions-V2":
        return html.Div([
            html.H3("Simulation de championnat (Prediction V2)"),

            # Ajout d'écurie
            html.Div([
                html.H5("Ajouter une écurie"),
                dcc.Input(id="constructor-input", type="text", placeholder="Entrer une écurie", debounce=True),
                html.Ul(id="constructor-suggestions", className="suggestions-list"),
            ], style={"width": "45%", "display": "inline-block", "verticalAlign": "top"}),

            html.Div([
                html.H5("Écuries sélectionnées"),
                html.Div(id="selected-constructors")
            ], style={"width": "50%", "display": "inline-block", "padding": "0 20px"}),

            html.Hr(),

            # Ajout de circuits
            html.Div([
                html.H5("Ajouter un circuit"),
                dcc.Input(id="circuit-input", type="text", placeholder="Entrer un circuit", debounce=True),
                html.Ul(id="circuit-suggestions", className="suggestions-list"),
            ], style={"width": "45%", "display": "inline-block", "verticalAlign": "top"}),

            html.Div([
                html.H5("Circuits sélectionnés"),
                html.Div(id="selected-circuits")
            ], style={"width": "50%", "display": "inline-block", "padding": "0 20px"}),

        ], style={"padding": "20px"})


# Callbacks pour la page pilotes (tu peux reprendre les tiens, avec ids modifiés si besoin)
@app.callback(
    Output("driver-list", "children"),
    Input("search-bar", "value")
)
def update_driver_list(search):
    filtered = [
        d for d in drivers_sorted
        if search is None or search.lower() in (d['forename'] + " " + d['surname']).lower()
    ]
    return [
        html.Div(
            f"{d['forename']} {d['surname']}",
            className="driver-card",
            n_clicks=0,
            id={'type': 'driver-card', 'index': d['driverId']}
        ) for d in filtered
    ]

@app.callback(
    Output("driver-details", "children"),
    Input({'type': 'driver-card', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def show_driver_details(n_clicks, **kwargs):
    ctx = callback_context
    if not ctx.triggered:
        return "Sélectionnez un pilote"
    driver_id = ctx.triggered[0]["prop_id"].split(".")[0]
    driver_id = eval(driver_id)['index']
    driver = next((d for d in drivers if d['driverId'] == int(driver_id)), None)
    return get_driver_details(driver)

# Callbacks pour la page constructeurs
@app.callback(
    Output("constructor-list", "children"),
    Input("search-bar-constructors", "value")
)
def update_constructor_list(search):
    filtered = [
        c for c in constructors_sorted
        if search is None or search.lower() in c['name'].lower()
    ]
    return [
        html.Div(
            c['name'],
            className="constructor-card",
            n_clicks=0,
            id={'type': 'constructor-card', 'index': c['constructorId']}
        ) for c in filtered
    ]

@app.callback(
    Output("constructor-details", "children"),
    Input({'type': 'constructor-card', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def show_constructor_details(n_clicks, **kwargs):
    ctx = callback_context
    if not ctx.triggered:
        return "Sélectionnez un constructeur"
    constructor_id = ctx.triggered[0]["prop_id"].split(".")[0]
    constructor_id = eval(constructor_id)['index']
    constructor = next((c for c in constructors if c['constructorId'] == int(constructor_id)), None)
    return get_constructor_details(constructor)



# Suggestions d’écuries
@app.callback(
    Output("constructor-suggestions", "children"),
    Input("constructor-input", "value")
)
def suggest_constructors(partial_name):
    if not partial_name:
        return []
    suggestions = [
        html.Li(c["name"], n_clicks=0, id={'type': 'suggested-constructor', 'index': c['constructorId']})
        for c in constructors_sorted if partial_name.lower() in c["name"].lower()
    ]
    return suggestions[:5]


# Ajouter une écurie sélectionnée
@app.callback(
    Output("selected-constructors", "children"),
    Input({'type': 'suggested-constructor', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def add_selected_constructor(n_clicks):
    ctx = callback_context
    if not ctx.triggered:
        return dash.no_update

    triggered_id = eval(ctx.triggered[0]["prop_id"].split(".")[0])
    constructor_id = triggered_id["index"]
    constructor = next((c for c in constructors if c['constructorId'] == constructor_id), None)

    if constructor and constructor["name"] not in selected_teams:
        selected_teams.append(constructor["name"])

    return [
        html.Div([
            html.Span(team),
            html.Div("➕ Ajouter pilotes", className="add-driver-button", style={"display": "none"})
        ], className="constructor-entry", id={"type": "constructor-entry", "index": i})
        for i, team in enumerate(selected_teams)
    ]


# Suggestions de circuits
@app.callback(
    Output("circuit-suggestions", "children"),
    Input("circuit-input", "value")
)
def suggest_circuits(partial_name):
    if not partial_name:
        return []
    suggestions = [
        html.Li(c["name"], n_clicks=0, id={'type': 'suggested-circuit', 'index': c['circuitId']})
        for c in circuits_sorted if partial_name.lower() in c["name"].lower()
    ]
    return suggestions[:5]


# Ajouter un circuit sélectionné
@app.callback(
    Output("selected-circuits", "children"),
    Input({'type': 'suggested-circuit', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def add_selected_circuit(n_clicks):
    ctx = callback_context
    if not ctx.triggered:
        return dash.no_update

    triggered_id = eval(ctx.triggered[0]["prop_id"].split(".")[0])
    circuit_id = triggered_id["index"]
    circuit = next((c for c in circuits if c['circuitId'] == circuit_id), None)

    if circuit and circuit["name"] not in selected_circuits:
        selected_circuits.append(circuit["name"])

    return [
        html.Div(c, className="circuit-entry")
        for c in selected_circuits
    ]


if __name__ == "__main__":
    app.run(debug=True)
