# from dash import Dash, html, dcc
# from dash import Dash, html, dcc,Input, Output, State, callback
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback
from datetime import date
from dash.exceptions import PreventUpdate
import time

import base64
import datetime
import io

import pandas as pd

from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# # app = Dash(__name__, external_stylesheets=external_stylesheets)
# app = DjangoDash('Plotly_Basic',prevent_initial_callbacks=True, external_stylesheets=external_stylesheets)
app = DjangoDash('Plotly_Basic',external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.H2('Dropdown'),
        html.Hr(),
        html.Div([
            html.H4('origin'),
            dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
            html.H4('multi'),
            dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal', multi=True)
        ]),

        html.H2('Slider'),
        html.Hr(),
        html.Div([
            html.H4('origin'),
            dcc.Slider(-5, 10, 1, value=-3),
            html.H4('origin_function'),
            dcc.Slider(0, 9, marks={i: f'Label{i}' for i in range(10)}, value=5),
            html.H4('RangeSlider'),
            dcc.RangeSlider(-5, 10, 1, count=1, value=[-3, 7]),
            html.H4('RangeSlider_function'),
            dcc.RangeSlider(-5, 6,
                            marks={i: f'Label{i}' for i in range(-5, 7)},
                            value=[-3, 4]
                            ),
        ]),
    ],style={'border': 'solid'}),
    html.Div([
        html.H2('INPUT'),
        html.Hr(),
        html.Div([
            html.H4('origin'),
            dcc.Input(
                placeholder='Enter a value...',
                type='text',
                value=''
            ),
        ]),
        html.H2('Textarea'),
        html.Hr(),
        html.Div([
            html.H4('origin'),
            dcc.Textarea(
                placeholder='Enter a value...',
                value='This is a TextArea component',
                style={'width': '100%'}
            ),
        ]),
        html.H2('Checkboxes'),
        html.Hr(),
        html.Div([
            html.H4('origin'),
            dcc.Checklist(['New York City', 'Montréal', 'San Francisco'],
                          ['Montréal', 'San Francisco']),
            html.H4('inline'),
            dcc.Checklist(
                ['New York City', 'Montréal', 'San Francisco'],
                ['Montréal', 'San Francisco'],
                inline=True
            ),
        ]),
        html.H2('Radio Items'),
        html.Hr(),
        html.Div([
            html.H4('origin'),
            dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
            html.H4('inline'),
            dcc.RadioItems(
                ['New York City', 'Montréal', 'San Francisco'],
                'Montréal',
                inline=True
            ),
        ]),
    ],style={'width': '49%', 'display': 'inline-block', 'border': 'solid'}),
    html.Div([
        html.H2('Button'),
        html.Hr(),
        html.Div([
            html.H4('Button'),
            html.Div(dcc.Input(id='input-box', type='text')),
            html.Button('Submit', id='button-example-1'),
            html.Div(id='output-container-button',
                     children='Enter a value and press submit'),
            html.H4('DatePickerSingle'),
            html.Div([
                dcc.DatePickerSingle(
                    id='date-picker-single',
                    date=date(1997, 5, 10)
                )
            ]),
            html.H4('DatePickerRange'),
            html.Div([
                dcc.DatePickerRange(
                    id='date-picker-range',
                    start_date=date(1997, 5, 3),
                    end_date_placeholder_text='Select a date!'
                )
            ]),
            html.H4('Dropdown'),
            html.Div([
                dcc.Markdown('''
                    #### Dash and Markdown
                    Dash supports [Markdown](http://commonmark.org/help).
                    Markdown is a simple way to write and format text.
                    It includes a syntax for things like **bold text** and *italics*,
                    [links](http://commonmark.org/help), inline `code` snippets, lists,
                    quotes, and more.
                ''')
            ]),

        ]),
    ],style={'width': '49%', 'float': 'right', 'display': 'inline-block', 'border': 'solid'}),
    html.Div([
        html.H2('Download Component'),
        html.Div(
            [html.Button("Download Text", id="btn_txt"), dcc.Download(id="download-text-index")]
        ),
        html.H2('Tabs'),
        html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                dcc.Tab(label='Tab one', value='tab-1'),
                dcc.Tab(label='Tab two', value='tab-2'),
            ]),
            html.Div(id='tabs-content')
        ]),
        html.H2('Graphs'),
        html.Div([
            dcc.Graph(
                figure=dict(
                    data=[
                        dict(
                            x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                               2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                            y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                               350, 430, 474, 526, 488, 537, 500, 439],
                            name='Rest of world',
                            marker=dict(
                                color='rgb(55, 83, 109)'
                            )
                        ),
                        dict(
                            x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                               2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                            y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                               299, 340, 403, 549, 499],
                            name='China',
                            marker=dict(
                                color='rgb(26, 118, 255)'
                            )
                        )
                    ],
                    layout=dict(
                        title='US Export of Plastic Scrap',
                        showlegend=True,
                        legend=dict(
                            x=0,
                            y=1.0
                        ),
                        margin=dict(l=40, r=0, t=40, b=30)
                    )
                ),
                style={'height': 300},
                id='my-graph-example'
            )
        ]),
        html.H2('ConfirmDialogProvider'),
        html.Div([
            dcc.ConfirmDialogProvider(
                children=html.Button(
                    'Click Me',
                ),
                id='danger-danger',
                message='Danger danger! Are you sure you want to continue?'
            )
        ]),
        html.H2('Store'),
        html.Div([
            dcc.Store(id='my-store'),
            dcc.RadioItems(['NYC', 'MTL', 'SF'], 'NYC', id='my-store-input'),
            html.Div(id='current-store')
        ]),
        html.H2('Loading Component'),
        html.Div([
            dcc.RadioItems(
                ["Montreal", "New York", "London"], "London", id="loading-demo-dropdown"
            ),
            dcc.Loading([html.Div(id="loading-demo")]),
        ]),
    ],style={'width': '49%', 'display': 'inline-block', 'border': 'solid'}),
    html.Div([
        html.Div([
            dcc.Upload(
                id='upload-image',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                # Allow multiple files to be uploaded
                multiple=True
            ),
            html.Div(id='output-image-upload'),
        ]),
    ],style={'width': '49%', 'float': 'right', 'display': 'inline-block', 'border': 'solid'}),
])

# Button
@callback(
    Output('output-container-button', 'children'),
    Input('button-example-1', 'n_clicks'),
    State('input-box', 'value'))
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )

# Download Component
@callback(Output("download-text-index", "data"), Input("btn_txt", "n_clicks"))
def func(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return dict(content="Hello world!", filename="hello.txt")

# Taps
@callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])

# Store
@callback(
    Output('my-store', 'data'),
    Input('my-store-input', 'value')
)
def update_store(value):
    return value

@callback(
    Output('current-store', 'children'),
    Input('my-store', 'modified_timestamp'),
    State('my-store', 'data')
)
def display_store_info(timestamp, data):
    return f"The store currently contains {data} and the modified timestamp is {timestamp}"

# Loading Component
@callback(Output("loading-demo", "children"), Input("loading-demo-dropdown", "value"))
def update_loading_div(value):
    time.sleep(2)
    return f"You selected {value}"

def parse_contents(contents, filename, date):
    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        html.Img(src=contents),
        html.Hr(),
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

# Displaying Uploaded Images
@callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children