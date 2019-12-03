#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:41:37 2019

@author: bastianjensen
"""

import pandas as pd

url = 'https://raw.githubusercontent.com/bastianjensen/PT_UNAB/procesamiento/procesamiento_visalizacion/radio_data_sun_DATE_keys.csv'


df = pd.read_csv(url)   ## lee un archivo CSV de github

print(df.head(5))       ## imprime las primeras X lineas

