#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 23:21:25 2019

@author: bastianjensen
"""


"""
import dash
import dash_core_components as dcc
import dash_html_components as html

## https://github.com/bastianjensen/PT_UNAB/blob/procesamiento/radio_data_sun_CONVERTED_TO_DATE.csv




## GRAFICA


app = dash.Dash()


app.layout = html.Div(children=[
  html.H1(children='Gráficos generados a partir de radio telescopio'),
  
  dcc.Graph(id='ejemplo',
    figure={
      'data': [
        {'x': [1, 2, 3, 4], 'y': [1, 8, 3, 7], 'type': 'line', 'name': 'Bicicletas'},
        {'x': [1, 2, 3, 4], 'y': [5, 2, 8, 8], 'type': 'bar', 'name': 'Bicicletas electricas'},
        ],
      'layout': {
      'title': 'Ejemplo básico en Dash'
        }
      })

  ])


    
if __name__ == '__main__':
  app.run_server(debug=True)
  
  
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
#https://raw.githubusercontent.com/bastianjensen/PT_UNAB/master/radio_data_sun_MEDIA_10000.csv
df = pd.read_csv('https://raw.githubusercontent.com/bastianjensen/PT_UNAB/procesamiento/procesamiento_visalizacion/radio_data_sun_DATE_keys.csv')  
#df = pd.read_csv('https://raw.githubusercontent.com/bastianjensen/PT_UNAB/procesamiento/radio_data_sun_CONVERTED_TO_DATE.csv')  

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')





external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['date'].min(),
        max=df['date'].max(),
        value=df['date'].min(),
        marks={str(date): str(date) for date in df['date'].unique()},
        step=None
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.date == selected_year]
    traces = []
    for i in filtered_df.date.unique():
        df_by_continent = filtered_df[filtered_df['date'] == i]
        traces.append(dict(
            x=df_by_continent['date'],
            y=df_by_continent['variation'],
            text=df_by_continent['signal'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'line', 'title': 'GDP Per Capita',
                   'range':[0, -1]},
            yaxis={'title': 'Life Expectancy', 'range': [0, 1024]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
        )
    }



if __name__ == '__main__':
    app.run_server(debug=True)
  