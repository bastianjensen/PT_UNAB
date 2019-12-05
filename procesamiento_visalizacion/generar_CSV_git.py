#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 01:15:17 2019
@author: bastianjensen
"""

import pandas as pd
from datetime import datetime, date
import datetime
import numpy as np
import shutil



def run(my_input_file_name):
    pass

input_file_name = "Datos_nov_30_dic_3_MEDIA_10000.csv"  #my_input_file_name


## abro solamente una vez el archivo y almaceno los datos en vriables para no ejecutar lectura en cada iteraccion
date_data = global_file.get('date')
battery_data = global_file.get('battery')
signal_data = global_file.get('signal')
variation_data = global_file.get('variation')



## generar archivos por rango de hora y por dia
## Dia:[listas_por_hora] -> Dia : [ []. []. [], []]


   
## global_file = pd.read_csv(input_file_name)  ## lee el archivo y genera un diccionario
global_file = pd.read_csv("Datos_nov_30_dic_3_MEDIA_10000.csv")

start_date_str = global_file.get('date')[0]
end_date_str = global_file.get('date')[ len(global_file)-1 ]

start_date = datetime.datetime.strptime( global_file.get('date')[0] , '%Y-%m-%d %H:%M:%S.%f')
end_date = datetime.datetime.strptime( global_file.get('date')[ len(global_file)-1 ] , '%Y-%m-%d %H:%M:%S.%f')

rango_tiempo = end_date - start_date
dias = rango_tiempo.days
horas = rango_tiempo.seconds/3600




def buscar_indice(valor_buscado):
    index = 0
    for index in range(len(date_data)):
        if(date_data[index] >= valor_buscado):
            return index
        index += 1



## nombre de archivos que se cargaran en GitHub para ser leidos con Dash
nombre_FFT_00 = 'FFT_00_00.csv'
nombre_FFT_06 = 'FFT_06_00.csv'
nombre_FFT_12 = 'FFT_12_00.csv'
nombre_FFT_18 = 'FFT_18_00.csv'
nombre_media_por_hora = "media_por_hora.csv"


## iniciar escritura y reescribir en caso de existir el archivo
FFT_00_file = open(nombre_FFT_00, 'w')
FFT_06_file = open(nombre_FFT_06, 'w')
FFT_12_file = open(nombre_FFT_12, 'w')
FFT_18_file = open(nombre_FFT_18, 'w')
media_por_hora_file = open(nombre_media_por_hora, 'w')

media_por_hora_file.write("date,battery,signal,variation\n")



## escribir archivo de secuencia temporal, copiar input_file_name a secuencia_temporal.csv
shutil.copy(input_file_name, "secuencia_temporal.csv")



rango_una_hora_date = [start_date + datetime.timedelta(seconds=x*3600) for x in range(0, int( (end_date-start_date).days * 24 +  (end_date-start_date).seconds/3600))]   # genera saltos de una hora


first_date = start_date



for i in range(len(rango_una_hora_date)-2):
    start_index = buscar_indice(rango_una_hora_date[i].strftime('%Y-%m-%d %X.%f'))
    end_index = buscar_indice(rango_una_hora_date[i+1].strftime('%Y-%m-%d %X.%f'))
    
    battery_media = str( int( np.mean(global_file.get('battery')[start_index:end_index]) ) )
    signal_media = str( int( np.mean(global_file.get('signal')[start_index:end_index]) ) )
    variation_media = str( int( np.mean(global_file.get('variation')[start_index:end_index]) ) )
    
    
    mean_index = int( np.mean(start_index + end_index) )
   
    line = rango_una_hora_date[i].strftime('%Y-%m-%d %X.%f') + ',' + battery_media + ',' + signal_media + ',' + variation_media + '\n'
    print(line)
    
    media_por_hora_file.write(line)
    
    
    
    ## agrego los FFT
    if(0 < rango_una_hora_date[i].hour < 1):
        ## si el rango se encuentra entre las 00:00 y 01:00 AM
        global_file[start_index:end_index]
        
    elif(6 < rango_una_hora_date[i].hour < 7):
        ## si el rango se encuentra entre las 00:00 y 01:00 AM
        global_file[start_index:end_index]
        
    elif(12 < rango_una_hora_date[i].hour < 13):
        ## si el rango se encuentra entre las 00:00 y 01:00 AM
        global_file[start_index:end_index]
        
    elif(18 < rango_una_hora_date[i].hour < 19):
        ## si el rango se encuentra entre las 00:00 y 01:00 AM
        global_file[start_index:end_index]
        
    
    
    
    
    i += 1


    

    
    
    
    
    
    
    
    
    
    
"""
for date_limite in rango_una_hora_date[1:]:
    print("entra en el for")
    start_index = buscar_indice(first_date.strftime('%Y-%m-%d %X.%f'))
    end_index = buscar_indice(date_limite.strftime('%Y-%m-%d %X.%f'))
    
    print("start index = " + str(buscar_indice(first_date.strftime('%Y-%m-%d %X.%f')))) #str(start_index))
    print("end index = " + str(buscar_indice(date_limite.strftime('%Y-%m-%d %X.%f')))) #str(end_index))
    print("date_limite = " + str(date_limite))
    print("data limite = " + date_limite.strftime('%Y-%m-%d %X.%f') + "\n")
    print("")
    
"""
    
"""
    mean_index = np.mean(start_index + end_index)
   
    

    
    rango_dates = global_file[start_index: end_index]    ## copia los datos que pertenecen a un rango definido
    
    battery_media = str( int( np.mean(rango_dates.get('battery')) ) )
    signal_media = str( int( np.mean(rango_dates.get('signal')) ) )
    variation_media = str( int( np.mean(rango_dates.get('variation')) ) )
    
    media_por_hora_file.write(str(mean_index) + ',' + battery_media + ',' + signal_media + ',' + variation_media + '\n')
    

"""







"""
while (start_date < end_date):  ## si es igual al ultimo dato registrado (criterio a partir de Date), termina el ciclo
    
    media_battery = 0
    media_signal = 0
    media_variation = 0
    
    contador_valores = 0
    
    ## archivo generado por hora
    #local_file_name = input_file_name.replace('.csv', '_' + str(start_date.year) + '_' + str(start_date.month) + '_' + str(start_date.hour) + 'HORA.csv')
    
    
    while(datetime.strptime(date_data[i], '%Y-%m-%d %H:%M:%S.%f').hour < start_date.hour + 1 and datetime.strptime(date_data[i], '%Y-%m-%d %H:%M:%S.%f') <= end_date):
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
    
"""



    












#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 01:15:17 2019

@author: bastianjensen
"""
"""
import pandas as pd
from datetime import datetime, date
import datetime, time


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
    
rango_tiempo = dia_n - dia_0 # datetime.strptime(dia_n - dia_0  )
dias = rango_tiempo.days
horas = rango_tiempo.seconds/3600
    
    
    
    
i = 0
    
start_date = dia_0
end_date = dia_n
    
nombre_archivos_FFT= ['FFT_00_00.csv', 'FFT_06_00', 'FFT_12_00.csv', 'FFT_18_00.csv']
    
    
    ## abro solamente una vez el archivo y almaceno los datos en vriables para no ejecutar lectura en cada iteraccion
date_data = global_file.get('date')
battery_data = global_file.get('battery')
signal_data = global_file.get('signal')
variation_data = global_file.get('variation')
    
    
    
"""

"""
    ## opcion 1
    start = datetime.strptime( global_file.get('date')[0] , '%Y-%m-%d %H:%M:%S.%f')
    end = datetime.strptime( global_file.get('date')[ len(global_file)-1 ] , '%Y-%m-%d %H:%M:%S.%f')
    
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, int((end-start).seconds/3600) )]   # genera saltos de una hora


def buscar_indice(valor_buscado):
    index = 0
    for index in range(len(date_data)):
        if(date_data[index] == valor_buscado):
            return index
        index += 1

"""

"""


## opcion 2

while (start_date < end_date):  ## si es igual al ultimo dato registrado (criterio a partir de Date), termina el ciclo
    
    media_battery = 0
    media_signal = 0
    media_variation = 0
    
    contador_valores = 0
    
    ## archivo generado por hora
    #datos_por_hora = input_file_name.replace('.csv', '_' + str(start_date.year) + '_' + str(start_date.month) + '_' + str(start_date.hour) + 'HORA.csv')
    print("primer while i = " +str(i) )
    
    while(datetime.strptime(date_data[i], '%Y-%m-%d %H:%M:%S.%f').hour < start_date.hour + 1 and datetime.strptime(date_data[i], '%Y-%m-%d %H:%M:%S.%f') <= end_date):
        
         print("segundo while i = " +str(i) )
         battery = battery_data[i]   #date = datetime.strptime(day, '%Y-%m-%d %H:%M:%S.%f')
         signal = signal_data[i]
         variation = variation_data[i]
            
         ## sumo el valor a media, que corresponde a una sumatoria temporal que luego es dividida para extraer su media
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
    
    
    ## Se escribe en un CSV la media de los datos obtenidos en una hora determinada (hora inicial en que se comenzo a calcular la media)
    media_por_hora.write( str(start_date) + ',' + str(media_battery) + ',' + str(media_signal) + ',' + str(media_variation) + '\n')
   
    
    
    ## actualiza el valor del Date inicial para la siguiente iteracion
    start_date = datetime.strptime(date_data[i], '%Y-%m-%d %H:%M:%S.%f') ## el i ya se encuentra incrementado
    

"""       
    
    
    
    
    