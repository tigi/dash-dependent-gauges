# -*- coding: utf-8 -*-
"""
Created on 3 march 2022

@auth: Marie-Anne Melis
"""

import dash
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc



app = dash.Dash(__name__)

app = dash.Dash(external_stylesheets=[ dbc.themes.FLATLY])

app.layout = dbc.Container([
    dbc.Row([dbc.Col([html.H1(id = 'H1', children = 'Dash, bootstrap and dependent Gauges')],xl=12,lg=12,md = 12,sm=12,xs = 12)],style = {'textAlign':'center', 'marginTop':30, 'marginBottom':30}),

    
    dbc.Row([ 
        dbc.Col([
    
    daq.Gauge(
        id='my-gauge-1',
        color={"gradient":True,"ranges":{"red":[0,6],"yellow":[6,8],"green":[8,10]}},
        label="Select first value",
        value=6
    ),
    dcc.Slider(
        id='my-gauge-slider-1',
        min=0,
        max=10,
        step=1,
        value=5
    )],xl=6,lg=6,md = 6,sm=12,xs = 12),
    dbc.Col([
    daq.Gauge(
        id='my-gauge-2',
        color={"gradient":True,"ranges":{"red":[0,6],"yellow":[6,8],"green":[8,10]}},
        label="Select second value",
        value=6
    ),
    dcc.Slider(
        id='my-gauge-slider-2',
        min=0,
        max=10,
        step=1,
        value=5
    )],xl=6,lg=6,md = 6,sm=12,xs = 12),
    ]),
    dbc.Row([ 
        dbc.Col([
    html.Br(),
    daq.Gauge(
        id='summary-gauge',
        color={"gradient":True,"ranges":{"red":[0,6],"yellow":[6,8],"green":[8,10]}},
        label='Average'
        )
    ],xl=12,lg=12,md = 12,sm=12,xs = 12),
    ])
         
],fluid = False)



@app.callback([Output(component_id= 'my-gauge-1', component_property = 'value'),
              Output(component_id='my-gauge-2', component_property='value') ],
              [Input('my-gauge-slider-1', 'value'),
               Input('my-gauge-slider-2', 'value')])

def update_singlegauges(slider1,slider2):
    return (slider1,slider2)

@app.callback([Output(component_id= 'summary-gauge', component_property = 'value')],
              [Input('my-gauge-slider-1', 'value'),
               Input('my-gauge-slider-2', 'value')])

def update_summarygauge(slider1,slider2):
    value_out = (slider1 + slider2) /2
    return [value_out]



if __name__ == '__main__':
    app.run_server()

