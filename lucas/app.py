from dash import Dash, html, dcc,dash_table
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv('lucas/dataset/clean_nyc-rolling-sales.csv', index_col=0)


app = Dash(__name__)
df_date = df.groupby('SALE DATE').sum().sort_values(by=['SALE DATE'])
df = df.sort_values(by=['SALE DATE'])

fig = px.bar(df.head(10000), x="SALE DATE", y="SALE PRICE", color="BOROUGH_NAME", barmode="group")

def generate_table(dataframe, max_rows=10):
        return html.Table([
            html.Thead(
                html.Tr([html.Th(col) for col in dataframe.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                ]) for i in range(min(len(dataframe), max_rows))
            ])
        ])

app.layout = html.Div(children=[
    html.H1(children='Hello Dash',  style={'textAlign': 'center', 'color': '#7FDBFF'}),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dash_table.DataTable(df.head(10).to_dict('records')),

    generate_table(df),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)