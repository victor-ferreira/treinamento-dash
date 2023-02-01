import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc

app = Dash(
  __name__,
  external_stylesheets=[dbc.themes.ZEPHYR, dbc.icons.FONT_AWESOME],
  meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

######### CREATING GLOBAL VARS #########

df = pd.read_pickle('data/online-retail(cleaned).pkl')

######### LAYOUT VARIABLES #########

app.layout = html.Div([
  html.Div([
    html.I(className="fa-solid fa-gauge"),
    html.H1('Procenge Data Dashboard'),
  ]),
  
  dash_table.DataTable(df.head(10).to_dict('records'))
])


if __name__ == '__main__':
  app.run_server(debug=True)
