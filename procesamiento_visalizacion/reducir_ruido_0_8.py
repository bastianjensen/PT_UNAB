# algoritmo reduccion de ruido por media ponderada

import psutil
import os
from time import time
import numpy as np




##	INPUT	debe recibir el formato
##	(Date) Date, (int) Signal, (int) Battery, (int) Variation

## ANTES : lee el formato: (int) Battery, (int) Signal , y calcula variacion 	-	CORREGIDO


##	OUTPUT	retorna una media por cada 10K datos
##	(Date) Date, (int) Signal, (int) Battery, (int) NoiseReduced (reemplaza Variation por NoiseReduced)

## ANTEs la salida tiene formato:	(int) Battery, (int) Signal, (int) Variation, (int) NoiseReduced 	-	CORREGIDO


def read_file(file_name):
	## LEE el archivo CSV y genera una array de NumPy
	data_array = np.loadtxt(file_name, delimiter=',')	## crea un array de floats
	data_array = np.asarray(data_array, int)
	return data_array


def set_file_name(file_name_input):
	return file_name_input



def set_delta_data(data_array, delta_data):
	for data in data_array:
		#delta_data.append(data[1]-data[0])
		delta_data.append(data[3])	## lee (int) Variation que se encuentra en el indice 3 (Date, Battery, Signal, Variation)

	return delta_data

def reduce_noise(data, noise_reduced_array):		## RECIBE como data un arreglo con la diferencia de valores (power - signal)
	range_of_data = 7

	## multiplos ponderados para indices 0 (dato evaluado) e indices simetricos colineales
	mult_index_0 = 1
	mult_index_1 = 1
	mult_index_2 = 2
	mult_index_3 = 4
	#mult_index_4 = 1
	sum_mult_index = mult_index_0 + 2*mult_index_1 + 2*mult_index_2 + 2*mult_index_3


	lenght_file = len(data)	##	cantidad de datos del archivo

## se determina el primer y ultimo dato que pueden ser procesados
## al tomar una media con los laterales, los extremos no pueden ser filtrdos

	first_index = int(0 + ((range_of_data-1)/2)) # 0 + 3 = 3
	last_index = int(lenght_file - 1 - ((range_of_data-1)/2))

# procesamiento

## primero ciclo de filtrado de datos para reduccion de ruido por filtro de media ponderada
	for index in range(first_index, last_index):
		noise_reduced_temporal_data = ( (data[index]*mult_index_0) + ( (data[index+1] + data[index-1])*mult_index_1 + (data[index+2] + data[index-2])*mult_index_2 + (data[index+3] + data[index-3])*mult_index_3 ) )/sum_mult_index 
		noise_reduced_array.append( noise_reduced_temporal_data )

	return noise_reduced_array
	

def media_filter(data, new_file, data_array):

#	start_time = time()

## segundo ciclo de filtrado

	lenght_noise_reduced_array = len(data)
	second_loop_range_of_data = 5	# rango de datos de filtro
	second_loop_first_index = int(0 + ((second_loop_range_of_data-1)/2))
	second_loop_last_index =int(lenght_noise_reduced_array - 1 - ((second_loop_range_of_data-1)/2))

	primary_index = first_index+second_loop_first_index # indice del primer elemento con respecto al data_array


	for index in range(second_loop_first_index, second_loop_last_index):
		second_loop_noise_reduced_array.append( int((data[index-2] + data[index-1] + data[index] + data[index+1] + data[index+2]) / second_loop_range_of_data) )


		new_file.write(str(data_array[primary_index+index][0]) + "," + str(data_array[primary_index+index][1]) + "," + str(delta_data[primary_index+index]) + "," + str(second_loop_noise_reduced_array[-1])+"\n")
		##new_file.write(str(data_array[primary_index+index][0]) + "," + str(data_array[primary_index+index][1]) + "," + str(delta_data[primary_index+index][2]) + "," + str(second_loop_noise_reduced_array[-1])+"\n")		## se quito el indice [2] de delta_data[primary_index+index][2]
		# index = (Date) Date, (int) Battery, (int) Signal, (int) NoiseReduced 

#	media_filter_time = time() - start_time

#	usage_time_median_filter.append( media_filter_time )
	
	#return second_loop_noise_reduced_array

def process_files():
	## solo se encarga de comunicarse con el usuario para pedir el nombre de un archivo a procesar
	## debe ser eliminado en integracion (o al menos, no ejecutado)

	file_name = 'jaula_faraday_9KHz_bandaDorada.csv' ## por defecto
	input_UI = input("ingresar nombre de archivo CSV a procesar (eliminar ruido): para omitir, ingrese 1: ")
	if(input_UI == str(1)):
		print("\nOk, Leyendo archivo " + file_name)
		return (read_file(file_name))
	else:
		if(input_UI.endswith(".csv")):
			return (read_file(str(input_UI)))
			print("\nLeyendo nuevo archivo " + str(input_UI))
		else:
			print("ERROR: verificar nombre del archivo ingresado, debe tener extensión .csv")
	return -1

##data_array = process_files()


def auto_ejectucion_no_integrada():
	## ejecuta el codigo, solicita ingresar manualmente el nombre de un archivo
	set_delta_data()
	reduce_noise(delta_data)
	media_filter(noise_reduced_array )
	#new_file.close()

def auto_ejectucion_integrada(file_name_input):
	## ejecuta el codigo, el nombre del archivo es ingresado al llamar a la funcion

	## se definen variables globales
	global second_loop_noise_reduced_array
	global len_data
	global first_index
	global last_index
	global write_file_name
	global data_array
	global delta_data
	global noise_reduced_array


	noise_reduced_array = list()
	delta_data = list()
	second_loop_noise_reduced_array = list()


	##	METADATA
	len_data = 0
	first_index = 3 # para range_of_data = 7


	file_name = set_file_name(file_name_input)	
	## el nombre ingresado es seteado


	## asigna nombre ingresado
	write_file_name = "noise_reduced_" + file_name + ".csv"


	## CREAR ARCHIVO
		#write_file = str(raw_input("ingresar nommbre del nuevo archivo: "))
	header = "Date,Signal,Battery,NoiseReduced\n"	## el header es omitido por el momento
	new_file = open(write_file_name, "w")
	#new_file.write(header)	

	data_array = read_file(file_name)	
	## lee el archivo con el nombre ingreasdo


	delta_data =  set_delta_data(data_array, delta_data)	
	## cargo el array delta_data que es una variable local dentro del ambito de la funcion auto_ejecucion_integrada()

	noise_reduced_array = reduce_noise(delta_data, noise_reduced_array)
	## el array delta_data es pasado a la funcion, y esta a su vez inserta valores en el array noise_reduced_array

	media_filter(noise_reduced_array, new_file, data_array)
	## recibe como parametro el array noise_reduced_array y carga valores en el archivo nuevo generado, en formato CSV
	#new_file.close()

	print("El archivo crudo ha sido procesado con exito en el modulo reducir_ruido")

	return ()



##auto_ejectucion_integrada("corregido.csv")



"""

set_file_name(file_name_input)
## recibe el nombre del archivo a procesar

read_file(file_name)
## lee el archvo con el nombre indicado

set_delta_data()
## crea una lista solo de las variaciones entre battery y signal

reduce_noise(data)
## primera etapa del algoritmo = reduccion por media ponderada

media_filter(data)
## segunda etapa del algoritmo = reduccion por media simple

process_files()
## solo se encarga de comunicarse con el usuario para pedir el nombre de un archivo a procesar
## debe ser eliminado en integracion (o al menos, no ejecutado)


auto_ejecucion_integrada()

"""
