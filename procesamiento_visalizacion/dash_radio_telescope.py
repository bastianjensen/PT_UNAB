#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 23:21:25 2019

@author: bastianjensen
"""

import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()
app.layout = html.Div(children=[
  html.H1(children='ráficos generados a partir de radio telescopio'),
  dcc.Graph()])
    
if __name__ == '__main__':
  app.run_server(debug=True)