import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html, dcc, register_page, page_registry

PAGE = {
  'name': 'Página 1',
}

register_page(__name__, name=PAGE['name'])

################# BEGINNING #################

layout = html.Div([
  html.H2(PAGE['name'])
])