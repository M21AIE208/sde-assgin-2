# Import packages
from dash import Dash, html,dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

import sqlite3
conn = sqlite3.connect('./database.sqlite')
iris_data = pd.read_sql_query("SELECT * FROM Iris", conn)
conn.close()


#Initialize the app
app = Dash(__name__,external_stylesheets=[dbc.themes.SIMPLEX])
server = app.server
# App layout
app.layout = html.Div(children=[
    html.Div(dbc.Row(dbc.Col(html.H1("SDE-assign-2",style={'textAlign': 'center'})))),
    html.Br(),
    html.Br(),
    html.Div(
            [
            dbc.Row(
                [
                    dbc.Col(
                        [
                        dbc.Row(dbc.Col(html.H5("Sepal width vs Petal width",style={'textAlign': 'center'}))),
                        dbc.Row(dcc.Graph(figure=px.scatter(iris_data, x='SepalWidthCm', y='PetalWidthCm', color="Species")))]
                        ,width=6

                    ),
                    dbc.Col(
                        [
                        dbc.Row(dbc.Col(html.H5("Sepal width vs Petal width",style={'textAlign': 'center'}))),
                        dbc.Row(dcc.Graph(figure=px.scatter(iris_data, x='SepalLengthCm', y='PetalLengthCm', color="Species")))]
                        ,width=6
                    ),

                ])
            ]
)

])


# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0")

