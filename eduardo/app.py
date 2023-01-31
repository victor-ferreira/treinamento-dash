import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, dash_table

app = Dash(__name__)

######### CREATING GLOBAL VARS #########

df = pd.read_pickle('data/online-reatail(cleaned).pkl')

######### LAYOUT VARIABLES #########

app.layout = html.Div(children=[
  html.H1(children='Procenge Data Dashboard'),
  
  dash_table.DataTable(df.head(10).to_dict('records'))
])
