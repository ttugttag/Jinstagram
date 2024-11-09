# import dash
# import dash_core_components as dcc
# import dash_html_components as html
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px                   # (version 4.7.0 or higher)
import pandas as pd
import plotly.graph_objects as go
from django_plotly_dash import DjangoDash


# ImportError: attempted relative import with no known parent package
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = DjangoDash('simpleexample', external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig_01 = px.line(df, x="Fruit", y="Amount", color="City")
fig_02 = px.scatter(df, x="Fruit", y="Amount", color="City")
fig_03 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])

data_a=fig
data_b=fig_02

app.layout = html.Div(
    # style={"background-color":"red", "overflow": "auto"},
    children=[
    dcc.Graph(
        id='example-graph',
        figure=data_a,
        # style={'width': '90px', 'height' : '500px'}
    ),
    dcc.Graph(
        id='example-graph',
        figure=data_b,
        # style={'width': '90px', 'height' : '500px'}
    )
])

print("실행실행")