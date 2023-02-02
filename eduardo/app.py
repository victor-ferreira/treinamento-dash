from dash import Dash, html, dcc, Input, Output, page_container, page_registry
import dash_bootstrap_components as dbc

app = Dash(
  __name__,
  external_stylesheets=[dbc.themes.ZEPHYR, dbc.icons.FONT_AWESOME],
  meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
  use_pages=True,
)

################# BEGINNING #################

sidebar = html.Div(
  [
    html.H1("Procenge Dashboard", className="display-6"),
    html.Hr(),
    html.P(
      "A simple sidebar layout with navigation links", className="lead"
    ),
    dbc.Nav(
      [
        dbc.NavLink(page['name'], href=page['path'], active="exact")
        for page in page_registry.values()
      ],
      vertical=True,
      pills=True,
    ),
  ],
  className='sidebar',
)

app.layout = html.Div(
  dbc.Row([
    dbc.Col(sidebar, width='auto'),
    dbc.Col(page_container, className='content'),
  ]),
  className='app-layout',
)



if __name__ == '__main__':
  app.run_server(debug=True)
