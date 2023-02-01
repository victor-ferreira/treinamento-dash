from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

app = Dash(
  __name__,
  external_stylesheets=[dbc.themes.ZEPHYR, dbc.icons.FONT_AWESOME],
  meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
  use_pages=True,
)

app.layout = html.Div([
])

if __name__ == '__main__':
  app.run_server(debug=True)
