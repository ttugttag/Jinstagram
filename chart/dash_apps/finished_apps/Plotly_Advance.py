# from dash import Dash, html
# import pandas as pd

# from dash import Dash, dcc, html
from dash import Dash, dcc, html, dash_table
import plotly.express as px
import pandas as pd

from django_plotly_dash import DjangoDash

# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
# print(df)

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

# def generate_table(dataframe, max_rows=143):
#     return html.Table([
#         html.Thead(
#             html.Tr([html.Th(col) for col in dataframe.columns])
#         ),
#         html.Tbody([
#             html.Tr([
#                 html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#             ]) for i in range(min(len(dataframe), max_rows))
#         ])
#     ])

df['pop'] = df['population'].apply(lambda x:
    '⭐⭐⭐' if x > 70000000 else (
    '⭐⭐' if x > 50000000 else (
    '⭐' if x > 30000000 else ''
)))
df['life'] = df['life expectancy'].apply(lambda x: '↗️' if x > 65 else '↘️')
df['gdp'] = df['gdp per capita'].apply(lambda x: '🔥' if x > 15000 else '🚒')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = DjangoDash('Plotly_Advance', external_stylesheets=external_stylesheets)

app.layout =  html.Div([
    # html.Div([
    #     html.H4(children='life-exp-vs-gdp'),
    #     generate_table(df)
    # ]),

    html.H4(children='life-exp-vs-gdp'),
    html.Div([
        dcc.Graph(
            id='life-exp-vs-gdp',
            figure=fig
        )
    ]),
    # generate_table(df),
    dash_table.DataTable(df.to_dict('records'), \
                         [{"name": i, "id": i} for i in df.columns],\
                         page_size=10, style_cell={'textAlign': 'left'}, \
                         style_cell_conditional = [
                            {
                                'if': {'column_id': 'gdp per capita'},
                                'textAlign': 'right',
                                'color': 'red'
                            }
                         ],
                         style_data={
                             'color': 'black',
                             'backgroundColor': 'white'
                         },
                         style_data_conditional=[
                             {
                                 'if': {'row_index': 'odd'},
                                 'backgroundColor': 'rgb(220, 220, 220)',
                                 'if': {
                                     'filter_query': '{{life expectancy}} = {}'.format(df['life expectancy'].min()),
                                 },
                                 'backgroundColor': '#FF4136',
                                 'color': 'white',
                             }
                         ],
                         style_header={
                             'backgroundColor': 'rgb(210, 210, 210)',
                             'color': 'black',
                             'fontWeight': 'bold'
                         })
])
