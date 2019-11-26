
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack


file_name = str(input("ingresar nombre de archivo procesado: "))

## CLI improvisada


data = list()


## funcion repetida
def read_file(file_name):
	## LEE el archivo CSV y genera una array de NumPy
	data_array = np.loadtxt(file_name, delimiter=',')	## crea un array de floats
	data_array = np.asarray(data_array, int)
	return data_array


def conver_data_to_array(extracted_data):
	for line in extracted_data:
		data.append(line[3])


conver_data_to_array(read_file(file_name))

print("largo de la lista = " + str(len(data)) )


## DATA se obtiene de un CSV ahora

## data ejemplo: [ 146, 110, 74, 48, 24, 9, -5, -8, -11, -10, -11, -11, -14, -15, -17, -18, -9, 6, 24, 48, 74, 105, 146, 192, 240, 290]
## asi debe ser el array que genera



# Number of samplepoints
#N = 512 #int(len(data))
N = len(data)

print("largo de DATA:\t\t" + str(N))
print(data[0:100])

# sample spacing
T = 1.0 / 8920						## sampling interval
Fs = 1/T 							## frecuency
x = np.linspace(0.0, N*T, N)		##	
y = data[0:7000] ##[100000:100000+(number_sample_points*2)] 	## 	LEE LINEA DEL ARCHIVO ABIERTO

yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)



## CONFIGURACION DE GRAFICO
fig, ax = plt.subplots()


ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
#plt.xlim(0, 4460)#4460)							##	rango eje X
plt.ylim(0, 20)					##	ranfo eje y
plt.grid()									## mostrar grid en el grafico

plt.xlabel('Frecuency (KHz)')						
plt.ylabel('Amplitude (mV)')
plt.title("FFT " + file_name)

plt.legend()




#plt.savefig("out.png")	## almacena una imagen en PNG


plt.show()









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
