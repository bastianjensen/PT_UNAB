#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 01:15:17 2019

@author: bastianjensen
"""

import pandas as pd
from datetime import datetime, date


global global_file

## generar archivos por rango de hora y por dia
## Dia:[listas_por_hora] -> Dia : [ []. []. [], []]


##
    


def run(input_file_name):
    pass

    
#global_file = pd.read_csv(input_file_name)  ## lee el archivo y genera un diccionario
global_file = pd.read_csv("Datos_nov_30_dic_3_MEDIA_10000.csv")

dia_0 = datetime.strptime( global_file.get('date')[0] , '%Y-%m-%d %H:%M:%S.%f')
dia_n = datetime.strptime( global_file.get('date')[ len(global_file)-1 ] , '%Y-%m-%d %H:%M:%S.%f')

rango_tiempo = datetime.strptime(dia_n - dia_0  )
dias = rango_tiempo.days
horas = rango_tiempo.seconds/3600


i = 0

start_date = dia_0
end_date = dia_n

while (start_date <= end_date):
    
    media_battery = 0
    media_signal = 0
    media_variation = 0
    contador_valores = 0
    
    while(datetime.strptime(global_file.get('date')[i], '%Y-%m-%d %H:%M:%S.%f').hour < start_date.hour + 1 and datetime.strptime(global_file.get('date')[i], '%Y-%m-%d %H:%M:%S.%f').hour <= end_date)
        #date = datetime.strptime(day, '%Y-%m-%d %H:%M:%S.%f')
        battery = global_file.get('battery')
        signal = global_file.get('signal')
        variation = global_file.get('variation')
        
        media_battery += battery
        media_signal += signal
        media_variation += variation
        contador_valores += 1
        
        i += 1  ## incrementa contador
    
    ## ya iterado por cada elemento encontrado en la misma hora
    media_battery /= contador_valores
    media_signal /= contador_valores
    media_variation /= contador_valores
    contador_valores = 0
    
    ## actualiza el valor del Date inicial para la siguiente iteracion
    start_date = datetime.strptime(global_file.get('date')[i], '%Y-%m-%d %H:%M:%S.%f') ## el i ya se encuentra incrementado
    
    
    ## Se escribe en un CSV la media de los datos obtenidos en una hora determinada (hora inicial en que se comenzo a calcular la media)
    media_por_hora.write( str(start_date) + ',' + str(media_battery) + ',' + str(media_signal) + ',' + str(media_variation) + '\n')
    

        
    
    
    
    
    