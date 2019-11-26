## algoritmo reduccion de ruido por media ponderada

import psutil
import os
from time import time

numero_datos = 1000


file_name = "sensorNoAislado_9KHz_movimiento.csv" ##PONER UN NOKBRE
#file = file('r', file_name)
for linea in file_name:
	print linea

file = [9.711557222, 22.37302366, 23.34768455, 13.22616108, 22.88711238, 10.27708171, 17.97721624, 5.76450386, 19.97616165, 13.68481567, 19.68940172, 13.72295873, 14.27458207, 6.619669356, 8.050942302, 24.70290949, 18.36434905, 16.47652521, 21.91841657, 10.38335064, 17.35336268, 7.277891712, 19.56206674, 17.36720484, 14.42293063, 22.2473534, 24.36975005, 17.94968284, 11.98753792, 17.32380899, 15.82745479, 9.776547948, 17.43646188, 17.84148896, 10.18488172, 6.420090816, 18.07300915, 20.46208712, 16.32102477, 11.41794477, 16.56573479, 12.82044454, 22.46769283, 13.80021103, 20.89210855, 16.77654389, 20.63290295, 24.58742118, 18.52793596, 11.32990246, 5.287826212, 15.14461742, 21.11150372, 4.873072848, 11.9753387, 9.99867053, 5.321066046, 10.0797084, 6.339414351, 8.875262564, 16.57365999, 21.85204216, 23.89324123, 24.68725577, 10.07148557, 16.96084147, 25.56142381, 12.96515277, 16.92697271, 19.0300639, 21.04700798, 12.30551184, 14.46597988, 5.915282881, 13.57722314, 9.336358771, 18.06892429, 23.87323016, 22.49241641, 25.9245999, 7.418722493, 8.257956409, 14.73548465, 17.12914416, 13.68142591, 10.18971574, 13.60887627, 18.06504033, 14.47663184, 21.37686409, 11.13171526, 24.94868405, 8.474128695, 19.58003368, 5.943840918, 13.42680696, 15.45673465, 8.819778389, 19.66363082, 5.111382142, 17.88247988, 9.515254193, 17.38493319, 6.312118013, 23.55907735, 16.81436542, 14.56937406, 21.49269765, 18.2090171, 6.688342032, 10.84905858, 21.57486916, 23.54219293, 12.05179297, 6.857026593, 5.581560872, 13.52160352, 4.031186936, 4.293004584, 14.28079748, 12.12147937, 13.46552339, 19.27249537, 4.615357144, 16.50301614, 18.11651518, 13.45118568, 22.15574095, 27.75997715, 28.4853181, 13.83628767, 11.97522897, 20.48623705, 11.136501, 8.443573196, 12.65545902, 23.94726809, 14.63425446, 23.59733128, 14.51444626, 21.69015367, 7.076515842, 18.08086654, 11.55934463, 13.5986158, 16.89098626, 19.1095176, 22.28947188, 16.62056748, 25.05161202, 11.90585451, 14.30268384, 21.77976904, 19.70975696, 21.50718161, 9.823882987, 14.3342881, 6.114582376, 5.821406088, 23.07583542, 7.657018373, 14.50728991, 10.14754322, 19.89887427, 18.70476463, 14.54779372, 12.65617025, 13.09793844, 4.363911069, 16.74339972, 6.098872911, 20.0462216, 9.94616505, 22.70972709, 12.61726462, 23.54707297, 16.00698841, 21.56132802, 18.24626488, 21.76920471, 8.291359745, 16.79666486, 16.65351339, 4.577696116, 14.00492499, 9.079375859, 9.461213879, 10.9518597, 26.9317799, 16.20276375, 11.22563483, 20.54537731, 25.19849188, 14.50137721, 13.62273605, 12.54646512, 23.83341931]

noise_reduced_array = list()
second_loop_noise_reduced_array = list()
start_time = 0.0
reduce_noise_time = 0.0
media_filter_time = 0.0

usage_time_reduce_noise = list()
usage_time_median_filter = list()



def reduce_noise(data):

	data = numero_datos*data
	start_time = time()

	range_of_data = 7

	## multiplos ponderados para indices 0 (dato evaluado) e indices simetricos colineales
	mult_index_0 = 1
	mult_index_1 = 1
	mult_index_2 = 2
	mult_index_3 = 4
	#mult_index_4 = 1


	lenght_file = len(data)	##	cantidad de datos del archivo

## se determina el primer y ultimo dato que pueden ser procesados
## al tomar una media con los laterales, los extremos no pueden ser filtrdos
	first_index = 0 + ((range_of_data-1)/2)
	last_index = lenght_file - 1 - ((range_of_data-1)/2)



# procesamiento

## primero ciclo de filtrado de datos para reduccion de ruido por filtro de media ponderada
	index = first_index
	for index in range(first_index, last_index):
		noise_reduced_array.append(  ( (data[index]*mult_index_0) + (data[index+1] + data[index-1])*mult_index_1 + (data[index+2] + data[index-2])*mult_index_2 + (data[index+3] + data[index-3])*mult_index_3 )/range_of_data  )
	#print(  (file[index]*mult_index_0 + (file[index+2]+file[index-2])*mult_index_1 + (file[index+3]+file[index-3])*mult_index_2 +(file[index+4]+file[index-4])*mult_index_3 )  / range_of_data)
	#(file[index+5]+file[index-5])*mult_index_4  / range_of_data
	
	reduce_noise_time = time() - start_time


	usage_time_reduce_noise.append( reduce_noise_time )
	return noise_reduced_array



def media_filter(data):

	start_time = time()

## segundo ciclo de filtrado

	lenght_noise_reduced_array = len(data)
	second_loop_range_of_data = 5	# rango de datos de filtro
	second_loop_first_index = 0 + ((second_loop_range_of_data-1)/2)
	second_loop_last_index =lenght_noise_reduced_array - 1 - ((second_loop_range_of_data-1)/2)


	for index in range(second_loop_first_index, second_loop_last_index):
		second_loop_noise_reduced_array.append( (data[index-2] + data[index-1] + data[index] + data[index+1] + data[index+2]) / second_loop_range_of_data )


	media_filter_time = time() - start_time

	usage_time_median_filter.append( media_filter_time )




noise_array = list()
median_array = list()

for x in range(10):
	numero_datos = 100*(x+1)
	##	cada iteracion aumenta el numero de datos (190*1000, 190*2000, 190*30000...)
	noise_sum = 0.0
	median_sum = 0.0

	print("indentacion #" + str(x))
	usage_time_reduce_noise = list()
	usage_time_median_filter = list()

	for i in range(10):
		noise_reduced_array = list()
		array = reduce_noise(file)
		media_filter(array)
		noise_sum += sum(usage_time_reduce_noise)
		median_sum += sum(usage_time_median_filter)

	print(noise_sum/10)
	noise_array.append(noise_sum/10)
	median_array.append(median_sum/10)

for i in range(1):
	print(noise_array)
	print(median_array)





print ("listo")


