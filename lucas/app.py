import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from pages import home, not_found_404




app = Dash(__name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP], 
    meta_tags=[{"name": "viewport", "content": "width=device-width"}], 
    suppress_callback_exceptions=True
    )

nav = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.NavLink(
                    "Início", href="/"
                    )
                )
        ],
        color="dark",
        dark=True,
    ), 
])

app.layout = html.Div([
    html.Div(
        [
            dcc.Location(id='url', refresh=False),
            nav, 
            html.Div(id='page-content', children=[])
        ]
    ),
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    else:
        return not_found_404.layout

if __name__ == '__main__':
	app.run_server(debug=True)

