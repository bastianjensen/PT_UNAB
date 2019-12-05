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





def buscar_indice(valor_buscado, date_data):
    index = 0
    for index in range(len(date_data)):
        if(date_data[index] >= valor_buscado):
            return index
        index += 1
        
        
def cargar_FFT(file_name):
    
    input_file_name = file_name##"Datos_nov_30_dic_3_MEDIA_10000.csv"  #my_input_file_name
    
    ## global_file = pd.read_csv(input_file_name)  ## lee el archivo y genera un diccionario
    global_file = pd.read_csv(input_file_name)
    
    ## abro solamente una vez el archivo y almaceno los datos en vriables para no ejecutar lectura en cada iteraccion
    date_data = global_file.get('date')
    #variation_data = global_file.get( global_file.keys()[3] )   ## variation
    
    
    
    ## generar archivos por rango de hora y por dia
    ## Dia:[listas_por_hora] -> Dia : [ []. []. [], []]
    
    
       
    
    
    start_date_str = global_file.get('date')[0]
    end_date_str = global_file.get('date')[ len(global_file)-1 ]
    
    start_date = datetime.datetime.strptime( global_file.get('date')[0] , '%Y-%m-%d %H:%M:%S.%f')
    end_date = datetime.datetime.strptime( global_file.get('date')[ len(global_file)-1 ] , '%Y-%m-%d %H:%M:%S.%f')
    
    rango_tiempo = end_date - start_date
    dias = rango_tiempo.days
    horas = rango_tiempo.seconds/3600
    
    
    
    
    
    
    
    ## nombre de archivos que se cargaran en GitHub para ser leidos con Dash
    nombre_FFT_00 = 'FFT_00_00.csv'
    nombre_FFT_06 = 'FFT_06_00.csv'
    nombre_FFT_12 = 'FFT_12_00.csv'
    nombre_FFT_18 = 'FFT_18_00.csv'
    #nombre_media_por_hora = "media_por_hora.csv"
    
    
    ## iniciar escritura y reescribir en caso de existir el archivo
    FFT_00_file = open(nombre_FFT_00, 'w')
    FFT_00_file.write("frecuencia,intensidad\n" )
    
    FFT_06_file = open(nombre_FFT_06, 'w')
    FFT_06_file.write("frecuencia,intensidad\n" )
    
    FFT_12_file = open(nombre_FFT_12, 'w')
    FFT_12_file.write("frecuencia,intensidad\n" )
    
    FFT_18_file = open(nombre_FFT_18, 'w')
    FFT_18_file.write("frecuencia,intensidad\n" )
    
    
    
    ## escribir archivo de secuencia temporal, copiar input_file_name a secuencia_temporal.csv
    #shutil.copy(input_file_name, "secuencia_temporal.csv")
    # esto lo hace con archivo de medias cada 5000 muestras
    
    
    rango_una_hora_date = [start_date + datetime.timedelta(seconds=x*3600) for x in range(0, int( (end_date-start_date).days * 24 +  (end_date-start_date).seconds/3600))]   # genera saltos de una hora
    
    
    first_date = start_date
    
    
    
    for i in range(len(rango_una_hora_date)-2):
        start_index = buscar_indice(rango_una_hora_date[i].strftime('%Y-%m-%d %X.%f'), date_data)
        end_index = buscar_indice(rango_una_hora_date[i+1].strftime('%Y-%m-%d %X.%f'), date_data)
        
        
        ## FFT
        
        Fs = 10     ## frecuencia en Hz
        T = 1/Fs    ## Periodo
        
        
        
        
        ## agrego los FFT
        if(0 < rango_una_hora_date[i].hour <= 1):
            ## si el rango se encuentra entre las 00:00 y 01:00 AM
            rango = global_file[start_index:end_index]
            if(len(rango) > 2000 ):
                lista_rango = rango['variation'][0:2000]#[0:2000]
            else:
                lista_rango = rango['variation']
            lista_rango = np.array(lista_rango)
            lista_rango = lista_rango.astype(int)
            
            eje_x = np.arange(0,10, 10/len(rango))  ## valores en x
            
            fft = np.fft.fft(lista_rango)    ## valores en eje y
    
            
            for valor in range( len(fft) ):
                FFT_00_file.write( str(eje_x[valor]) + ',' + str( float(fft[valor]) ) + '\n') 
            
            
        elif(6 < rango_una_hora_date[i].hour <= 7):
            ## si el rango se encuentra entre las 00:00 y 01:00 AM
            rango = global_file[start_index:end_index]
            lista_rango = rango['variation']
            
            eje_x = np.arange(0,10, 10/len(rango))  ## valores en x
            
            fft = np.fft.fft(lista_rango)    ## valores en eje y
            
            
            for valor in range( len(fft) ):
                FFT_06_file.write( str(eje_x[valor]) + ',' + str( float(fft[valor]) ) + '\n') 
            
            
        elif(12 < rango_una_hora_date[i].hour <= 13):
            ## si el rango se encuentra entre las 00:00 y 01:00 AM
            rango = global_file[start_index:end_index]
            lista_rango = rango['variation']
            
            eje_x = np.arange(0,10, 10/len(rango))  ## valores en x
            
            fft = np.fft.fft(lista_rango)    ## valores en eje y
            
            
            for valor in range( len(fft) ):
                FFT_12_file.write( str(eje_x[valor]) + ',' + str( float(fft[valor]) ) + '\n') 
            
            
        elif(18 < rango_una_hora_date[i].hour <= 19):
            ## si el rango se encuentra entre las 00:00 y 01:00 AM
            rango = global_file[start_index:end_index]
            lista_rango = rango['variation']
            
            eje_x = np.arange(0,10, 10/len(rango))  ## valores en x
            
            fft = np.fft.fft(lista_rango)    ## valores en eje y
            
            
            for valor in range( len(fft) ):
                FFT_18_file.write( str(eje_x[valor]) + ',' + str( float(fft[valor]) ) + '\n') 
        
        i += 1

    
    
def cargar_medias(file_name):
    


    input_file_name = file_name##"Datos_nov_30_dic_3_MEDIA_10000.csv"  #my_input_file_name
    
    ## global_file = pd.read_csv(input_file_name)  ## lee el archivo y genera un diccionario
    global_file = pd.read_csv(input_file_name)
    
    ## abro solamente una vez el archivo y almaceno los datos en vriables para no ejecutar lectura en cada iteraccion
    date_data = global_file.get('date')
    battery_data = global_file.get('battery')
    signal_data = global_file.get('signal')
    variation_data = global_file.get('variation')
    
    
    
    ## generar archivos por rango de hora y por dia
    ## Dia:[listas_por_hora] -> Dia : [ []. []. [], []]
    
    
       
    
    
    start_date_str = global_file.get('date')[0]
    end_date_str = global_file.get('date')[ len(global_file)-1 ]
    
    start_date = datetime.datetime.strptime( global_file.get('date')[0] , '%Y-%m-%d %H:%M:%S.%f')
    end_date = datetime.datetime.strptime( global_file.get('date')[ len(global_file)-1 ] , '%Y-%m-%d %H:%M:%S.%f')
    
    rango_tiempo = end_date - start_date
    dias = rango_tiempo.days
    horas = rango_tiempo.seconds/3600
    
    
    
    
    
    
    
    ## nombre de archivos que se cargaran en GitHub para ser leidos con Dash
    #nombre_FFT_00 = 'FFT_00_00.csv'
    #nombre_FFT_06 = 'FFT_06_00.csv'
    #nombre_FFT_12 = 'FFT_12_00.csv'
    #nombre_FFT_18 = 'FFT_18_00.csv'
    nombre_media_por_hora = "media_por_hora.csv"
    
    
    ## iniciar escritura y reescribir en caso de existir el archivo
    """
    FFT_00_file = open(nombre_FFT_00, 'w')
    FFT_00_file.write("frecuencia,intensidad\n" )
    
    FFT_06_file = open(nombre_FFT_06, 'w')
    FFT_06_file.write("frecuencia,intensidad\n" )
    
    FFT_12_file = open(nombre_FFT_12, 'w')
    FFT_12_file.write("frecuencia,intensidad\n" )
    
    FFT_18_file = open(nombre_FFT_18, 'w')
    FFT_18_file.write("frecuencia,intensidad\n" )
    """
    
    media_por_hora_file = open(nombre_media_por_hora, 'w')
    
    media_por_hora_file.write("date,battery,signal,variation\n")
    
    
    
    ## escribir archivo de secuencia temporal, copiar input_file_name a secuencia_temporal.csv
    shutil.copy(input_file_name, "secuencia_temporal.csv")
    
    
    
    rango_una_hora_date = [start_date + datetime.timedelta(seconds=x*3600) for x in range(0, int( (end_date-start_date).days * 24 +  (end_date-start_date).seconds/3600))]   # genera saltos de una hora
    
    
    first_date = start_date
    
    
    
    for i in range(len(rango_una_hora_date)-2):
        start_index = buscar_indice(rango_una_hora_date[i].strftime('%Y-%m-%d %X.%f'), date_data)
        end_index = buscar_indice(rango_una_hora_date[i+1].strftime('%Y-%m-%d %X.%f'), date_data)
        
        battery_media = str( int( np.mean(global_file.get('battery')[start_index:end_index]) ) )
        signal_media = str( int( np.mean(global_file.get('signal')[start_index:end_index]) ) )
        variation_media = str( int( np.mean(global_file.get('variation')[start_index:end_index]) ) )
        
        
        mean_index = int( np.mean(start_index + end_index) )
       
        line = rango_una_hora_date[i].strftime('%Y-%m-%d %X.%f') + ',' + battery_media + ',' + signal_media + ',' + variation_media + '\n'
        
        media_por_hora_file.write(line)
        
        
        
        """
        
        ## FFT
        
        Fs = 10     ## frecuencia en Hz
        T = 1/Fs    ## Periodo
        
        
        
        
        ## agrego los FFT
        if(0 < rango_una_hora_date[i].hour <= 1):
            ## si el rango se encuentra entre las 00:00 y 01:00 AM
            rango = global_file[start_index:end_index]
            
            eje_x = np.arange(0,10, 10/len(rango))  ## valores en x
            
            fft = np.fft.fft(rango['variation'])    ## valores en eje y
            
            
            
            for valor in range( len(fft) ):
                FFT_00_file.write( str(eje_x[valor]) + ',' + str( int(fft[valor]) ) + '\n') 
            
            
        elif(6 < rango_una_hora_date[i].hour <= 7):
            ## si el rango se encuentra entre las 00:00 y 01:00 AM
            rango = global_file[start_index:end_index]
            
            eje_x = np.arange(0,10, 10/len(rango))  ## valores en x
            
            fft = np.fft.fft(rango['variation'])    ## valores en eje y
            
            
            for valor in range( len(fft) ):
                FFT_06_file.write( str(eje_x[valor]) + ',' + str( int(fft[valor]) ) + '\n') 
            
            
        elif(12 < rango_una_hora_date[i].hour <= 13):
            ## si el rango se encuentra entre las 00:00 y 01:00 AM
            rango = global_file[start_index:end_index]
            
            eje_x = np.arange(0,10, 10/len(rango))  ## valores en x
            
            fft = np.fft.fft(rango['variation'])    ## valores en eje y
            
            
            for valor in range( len(fft) ):
                FFT_12_file.write( str(eje_x[valor]) + ',' + str( int(fft[valor]) ) + '\n') 
            
            
        elif(18 < rango_una_hora_date[i].hour <= 19):
            ## si el rango se encuentra entre las 00:00 y 01:00 AM
            rango = global_file[start_index:end_index]
            
            eje_x = np.arange(0,10, 10/len(rango))  ## valores en x
            
            fft = np.fft.fft(rango['variation'])    ## valores en eje y
            
            
            for valor in range( len(fft) ):
                FFT_18_file.write( str(eje_x[valor]) + ',' + str( int(fft[valor]) ) + '\n') 
            
            
        """
        
        
        
        i += 1


    
def run(my_input_file_name, my_long_file_name):
    
    
    pass