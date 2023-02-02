import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html, dcc, register_page, page_registry, dash_table

PAGE = {
  'name': 'Análise',
}

register_page(__name__, name=PAGE['name'])

df = pd.read_pickle('data/online-retail-cleaned.pkl')

################# BEGINNING #################

layout = html.Div([
  html.H2(PAGE['name']),
  dash_table.DataTable(
    data=df.head(10_000).to_dict('records'),
    columns=[{"name": i, "id": i, 'selectable': True} for i in df.columns],
    filter_action="native",
    sort_action="native",
    sort_mode="multi",
    page_action="native",
    page_current= 0,
    page_size= 10,
  ),
])
