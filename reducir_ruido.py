# algoritmo reduccion de ruido por media ponderada

import psutil
import os
from time import time
import numpy as np


noise_reduced_array = list()
delta_data = list()
second_loop_noise_reduced_array = list()



##	METADATA
len_data = 0
first_index = 3 # para range_of_data = 7


def read_file(file_name):
	## LEE el archivo CSV y genera una array de NumPy
	data_array = np.loadtxt(file_name, delimiter=',')	## crea un array de floats
	data_array = np.asarray(data_array, int)
	return data_array



## CLI improvisada
write_file_name = str(input("ingresar nombre de archivo a escribir: "))
write_file_name = "noise_reduced_" +write_file_name + ".csv"

## CREAR ARCHIVO
	#write_file = str(raw_input("ingresar nommbre del nuevo archivo: "))
header = "power,signal,delta,filtered\n"
new_file = open(write_file_name, "w")
#new_file.write(header)



def set_delta_data():
	for data in data_array:
		delta_data.append(data[1]-data[0])


def reduce_noise(data):		## RECIBE como data un arreglo con la diferencia de valores (power - signal)
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
	

def media_filter(data):

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

#	media_filter_time = time() - start_time

#	usage_time_median_filter.append( media_filter_time )
	
	#return second_loop_noise_reduced_array

def process_files():
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

data_array = process_files()


def noise_reduction():
	set_delta_data()
	reduce_noise(delta_data)
	media_filter(noise_reduced_array )
	#new_file.close()

noise_reduction()


print("escrito el archivo:\t" + write_file_name)

