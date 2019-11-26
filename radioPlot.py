import numpy as np
import matplotlib.pyplot as plt
import math


file_name = "resultado_filtro_2.csv"


## Lee el archivo CSV y genera un array de NumPy
data_array = np.loadtxt(file_name, delimiter=',')	## crea un array de floats
data_array = np.asarray(data_array, int)

print(data_array)


def get_by_index(index):
	local_list = list()
	for value in data_array:
		print(value[index])
		local_list.append(value[index])
	return local_list


def get_power_array():
	return ( get_by_index(0) )

def get_signal_array():
	return ( get_by_index(1) )

def get_delta_array():
	return ( get_by_index(2) )

def get_noissless_array():
	return ( get_by_index(3) )

"""
delta4 = delta[::2]
delta2 = delta[::4]		## 4.465KHz	
delta1 = delta[::8]		## 2.2325KHz
delta02 = delta[::64]	## 1.116KHz	
delta005 = delta[::256]
delta001 = delta[::1024]
"""

print(get_power_array())



plot_noissless_array = get_signal_array()
plt.plot( plot_noissless_array[0:1000] )

#plt.hist(numbers, bins = 3)
plt.xlabel("Muestra (#)")
plt.ylabel("Intensidad de sennal 12 bits (0 - 1024)")
plt.show()




