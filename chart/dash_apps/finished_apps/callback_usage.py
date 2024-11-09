import dash
# import dash_core_components as dcc
# import dash_html_components as html
from dash import Dash, html, dcc
from django_plotly_dash import DjangoDash

a2 = DjangoDash("callback_usage")

a2.layout = html.Div([
    dcc.RadioItems(id="dropdown-one",options=[{'label':i,'value':j} for i,j in [
    ("O2","Oxygen"),("N2","Nitrogen"),("CO2","Carbon Dioxide")]
    ],value="Oxygen"),
    html.Div(id="output-one")
    ])

# @a2.callback(
#     dash.dependencies.Output('output-one','children'),
#     [dash.dependencies.Input('dropdown-one','value')]
#     )
# def callback_c(*args,**kwargs):
#     da = kwargs['dash_app']
#     # return "Args are [%s] and kwargs are %s" %(",".join(args), kwargs)
#     return "Args are [%s] and kwargs are %s" %(",".join(args), ",".join(kwargs))

@a2.callback(
    dash.dependencies.Output('output-one','children'),
    [dash.dependencies.Input('dropdown-one','value')]
    )
def callback_c(*args, dash_app):
    return "Args are [%s] and the extra parameter dash_app is %s" %(",".join(args), dash_app)

# @a2.callback(
#     dash.dependencies.Output('output-one','children'),
#     [dash.dependencies.Input('dropdown-one','value')]
#     )
# def callback_c(*args, dash_app, **kwargs):
#     return "Args are [%s], the extra parameter dash_app is %s and kwargs are %s" %(",".join(args), dash_app, kwargs)