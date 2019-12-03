
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack


##	INPUT	



##	OUTPUT	

global data
global data_array
global file_name


## global dimens plot
global N 		## Numero de muestras por segundo
global T 		## Periodo (Sample interval)
global Fs 		## Frecuencia
global x 		## 
global y 		## 
global xf 		## 
global yf 		## 





data = list()
data_array = list()
file_name = ""


"""


def set_N(input_N):
	N = input_N

def get_N():
	return N

def set_T(input_T):
	T = input_T

def get_T():
	return T

def set_Fs(input_Fs):
	Fs = input_Fs

def get_Fs():
	return Fs

def set_x(input_x):
	x = input_x

def get_x():
	return x

def set_y(input_y):
	y = input_y

def get_y():
	return y

def set_yf(input_yf):
	yf = input_yf

def get_yf():
	return yf

def set_xf(input_xf):
	xf = input_xf

def get_xf():
	return xf
"""


## funcion repetida
def read_file(file_name):
	## LEE el archivo CSV y genera una array de NumPy
	data_array = np.loadtxt(file_name, delimiter=',')	## crea un array de floats
	data_array = np.asarray(data_array, int)
	return data_array


def conver_data_to_array(extracted_data):
	for line in extracted_data:
		data.append(line[file_index])

def save_file(xf, yf, file_name):
    if( len(xf) > len(yf) ):
        yf = yf[0:len(xf)+1]
    ## en caso de que el largo de los valores en x sea mayor que los valores en y, x se acorta e iguala a y
    
    for i in len(xf):
        file_name.write(  str(xf[i]) + ',' + str(xy[i]) )
    
    



def generar_FFT(data_array, input_file_name, axis_x_label, axis_y_label):
	#conver_data_to_array(read_file(file_name))

	#print("largo de la lista = " + str(len(data)) )


	## DATA se obtiene de un CSV ahora

	## data ejemplo: [ 146, 110, 74, 48, 24, 9, -5, -8, -11, -10, -11, -11, -14, -15, -17, -18, -9, 6, 24, 48, 74, 105, 146, 192, 240, 290]
	## asi debe ser el array que genera

	data = data_array
	file_name = input_file_name

	# Number of samplepoints
	#N = 512 #int(len(data))
	N = len(data)

	#print("largo de DATA:\t\t" + str(N))
	#print(data[0:100])

	# sample spacing
	T = 1.0 / 8920						## sampling interval
	Fs = 1/T 							## frecuency
	x = np.linspace(0.0, N*T, N)		##	
	y = data[0:7000] ##[100000:100000+(number_sample_points*2)] 	## 	LEE LINEA DEL ARCHIVO ABIERTO

	yf = scipy.fftpack.fft(y)
	xf = np.linspace(0.0, 1.0/(2.0*T), N/2)


	set_N(10)
	set_T(1/N)
	set_Fs(11000000000)
	#set_x()
	#set_y()
	#set_xf()
	#set_yf()



	## CONFIGURACION DE GRAFICO
	fig, ax = plt.subplots()


	ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
	#plt.xlim(0, 4460)#4460)					##	rango eje X
	plt.ylim(0, 20)								##	ranfo eje y
	plt.grid()									## mostrar grid en el grafico

	plt.xlabel(axis_x_label)					##'Frecuency (KHz)'					
	plt.ylabel(axis_y_label)					## 'Amplitude (mV)'
	plt.title("FFT " + file_name)

	plt.legend()




	#plt.savefig("out.png")	## almacena una imagen en PNG


	plt.show()
    

print("El modulo FFT_plot ha sido ejecutado correctamente")









##my_file = open("radio_data_sun_copy.csv", "r")

my_data = np.loadtxt('radio_data_sun_copy_CORRECTED.csv', comments = '#', delimiter=',')




promedio = np.mean(my_data[0:7000])



## divide cada elemento del array por media
data_array_x = my_data / promedio



generar_FFT(data_array_x[0:7000], "Datos crudos", "frecuencia (Hz)", "Intensidad (mA)")

## 	LEE ARCHIVOS TXT






"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack


file_name = "noise_reduced_request.txt"

## LEE ARCHIVO GENERADO EN noise_filter.py LLAMADO noise_reduced_request.txt
noise_reduced_file = open(file_name,"r")
data = noise_reduced_file.read()[1:-1].split(',')
index = 0
for index in range(len(data)):
	data[index] = int(data[index])
	index += 1
## lee datos del archivo y los convierte a lista de numeros



print(data)


# Number of samplepoints
#N = 600
N = 8920 #int(len(data))

# sample spacing
T = 1.0 / 8920						## sampling interval
Fs = 1/T 							## frecuency
x = np.linspace(0.0, N*T, N)		##	
y = data[100000:100000+(N*2)] 	## 	LEE LINEA DEL ARCHIVO ABIERTO

yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)


## CONFIGURACION DE GRAFICO
fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.xlim(0, 4460)#4460)							##	rango eje X
plt.ylim(0, 1024)					##	ranfo eje y
plt.grid()									## mostrar grid en el grafico

plt.xlabel('Frecuency (KHz)')						
plt.ylabel('Amplitude (mV)')
plt.title("FFT " + file_name)

plt.legend()




#plt.savefig("out.png")	## almacena una imagen en PNG


plt.show()
"""
