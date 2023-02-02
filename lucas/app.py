from dash import Dash, html, dcc,dash_table
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
# Load data
df = pd.read_csv('lucas/dataset/clean_nyc-rolling-sales.csv')


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{"name": "viewport", "content": "width=device-width"}], suppress_callback_exceptions=True)


df = df.sort_values(by=['SALE DATE'])

fig = px.bar(df.head(10000), x="SALE DATE", y="SALE PRICE", color="BOROUGH_NAME", barmode="group")

# def generate_table(dataframe, max_rows=10):
#         return html.Table([
#             html.Thead(
#                 html.Tr([html.Th(col) for col in dataframe.columns])
#             ),
#             html.Tbody([
#                 html.Tr([
#                     html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#                 ]) for i in range(min(len(dataframe), max_rows))
#             ])
#         ])

fig2 = px.scatter(df, x="RESIDENTIAL UNITS", y="SALE PRICE", color="BOROUGH_NAME", size="SALE PRICE", hover_name="NEIGHBORHOOD",
                 log_x=True, size_max=60)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash',  style={'textAlign': 'center', 'color': '#7FDBFF'}),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dbc.Row(children=[
        dbc.Col(html.Div(children=[
            html.Label('Dropdown'),
            dbc.Card(
                width=24,
                children=[
                        dbc.CardHeader(title='Nº de registros'),
                        dbc.DataCard(value=df.shape[0],
                                style={'width':'fit-content'}),
                ]
            ),
        ]), width=4),
        dbc.Col(html.Div(children=[
            html.Label('Radio Items'),
            dbc.Card(
                width=24,
                children=[
                        dbc.CardHeader(title='Valores nulos'),
                        dbc.DataCard(value=df.isnull().sum().sum(),
                                style={'width':'fit-content'}),
                ]
            ),
        ]), width=4),
        dbc.Col(html.Div(children=[
            html.Label('Checkboxes'),
            dbc.Card(
                width=24,
                children=[
                        dbc.CardHeader(title='Valores duplicados'),
                        dbc.DataCard(value=df.duplicated().sum(),
                                style={'width':'fit-content'}),
                ]
            ),
        ]), width=4),
    ]),

    dash_table.DataTable(
        df.head(10).to_dict('records'),
        style_cell={
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'maxWidth': 0
        }
    ),

    

    # generate_table(df),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(df["NEIGHBORHOOD"].unique().tolist(),
                    multi=True
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    
    dcc.Graph(
        id='example-graph2', 
        figure=fig2
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)