from dash import Dash, html, dcc,dash_table
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Load data
df = pd.read_csv('lucas/dataset/clean_nyc-rolling-sales.csv')

df = df.sort_values(by=['SALE DATE'])

df_sorted_by_price = df.sort_values(by=['SALE PRICE'], ascending=False)

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

fig2 = px.scatter(df, x="TOTAL UNITS", y="SALE PRICE", color="BOROUGH_NAME", size="SALE PRICE", hover_name="NEIGHBORHOOD", size_max=50)

layout = html.Div(children=[
    html.H1(children='Dashboard Venda de Casas',  style={'textAlign': 'center', 'marginBottom': 50, 'marginTop': 50}),

    html.Div([
        dbc.Row([
            dbc.Col(html.Div(
                [
                    dbc.Card([
                        dbc.CardHeader([
                            html.H6("Nº de registros")
                            ]),
                        dbc.CardBody([
                            html.H2(df.shape[0]),
                        ]),
                    ], color="dark", outline=True),
                ]), 
                width=2,
                md={"size": 2}
            ),
            dbc.Col(
                html.Div([
                    dbc.Card([
                            dbc.CardHeader([
                                html.H6("Nº de valores nulos")
                            ]),
                            dbc.CardBody([
                                html.H2(df.isnull().sum().sum()),
                            ]),
                        ], color="dark", outline=True
                    ),
                ]), 
                width=2,
                md={"size": 2}
            ),
            dbc.Col(
                html.Div([
                    dbc.Card([
                            dbc.CardHeader([
                                html.H6("Valores duplicados")
                            ]),
                            dbc.CardBody([
                                html.H2(df.duplicated().sum()),
                            ]),
                        ], color="dark", outline=True
                    ),
                ]),
                width=2,
                md={"size": 2}
            ), 
            dbc.Col(
                html.Div([
                    dbc.Card([
                            dbc.CardHeader([
                                html.H6("Valor total")
                            ]),
                            dbc.CardBody([
                                html.H2(
                                    locale.currency(df["SALE PRICE"].sum(), grouping=True)
                                ),
                            ]),
                        ], color="dark", outline=True
                    ),
                ]),
                width=2,
                md={"size": 3}
            )], 
            align="center", 
            justify="center"
        ),
    ], style={'marginBottom': 25, 'marginTop': 50}),

    # html.Div([
    #     dash_table.DataTable(
    #         df.head(10).to_dict('records'),
    #         style_cell={
    #         'overflow': 'hidden',
    #         'textOverflow': 'ellipsis',
    #         'maxWidth': 0
    #         }
    #     ),
    # ]),

    

    # generate_table(df),

    # html.Label('Multi-Select Dropdown'),
    # dcc.Dropdown(df["NEIGHBORHOOD"].unique().tolist(),
    #                 multi=True
    # ),
    html.Div([
        dcc.Graph(
            id='example-graph',
            figure=fig
        ),
        
        dcc.Graph(
            id='example-graph2', 
            figure=fig2
        ),
    ], style={'marginLeft': 200, 'marginRight': 200}),
])