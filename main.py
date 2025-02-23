import dash
import dash_bootstrap_components as dbc
from layouts.common_layout import create_main_layout
from callbacks.season_callbacks import register_race_callbacks, register_standings_callbacks
from callbacks.navigation_callbacks import register_navigation_callbacks
from data.f1_data import F1Data

# Créer l'application Dash avec Bootstrap et Bootstrap Icons
app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css'
    ]
)

# Récupérer les données
races_data = F1Data.get_races()

# Définir le layout principal
app.layout = create_main_layout()

# Enregistrer tous les callbacks
register_race_callbacks(app, races_data)
register_standings_callbacks(app)
register_navigation_callbacks(app)

# Lancer l'application
if __name__ == '__main__':
    app.run(debug=True)