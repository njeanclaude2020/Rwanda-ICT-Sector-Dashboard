import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import sys, os

# Add root to path so 'utils' can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # This is for deployment
sidebar = html.Div([
    html.H2("ICT SECTOR", className="text-white"),
    html.Hr(),
    dbc.Nav([
        dbc.NavLink("Home", href="/", active="exact"),
        dbc.NavLink("MINICT", href="/minict", active="exact"),
        dbc.NavLink("RISA", href="/risa", active="exact"),
        dbc.NavLink("NIDA", href="/nida", active="exact"),
    ], vertical=True, pills=True),
], className="sidebar") # Styled in your custom.css

app.layout = html.Div([
    sidebar,
    html.Div(dash.page_container, className="content") # Pages load here
])

if __name__ == "__main__":
    app.run(debug=True, port=8051)