## UI por linea de comando
from adaptacion_datos_0_8 import *
from reducir_ruido_0_8 import *
from corrector_de_formato import *
from FFT_plot_0_81 import *

datos = ""
file_name = ""


def read_file(file_name, index):
	## lee un archivo y retorna un array
	## si se quiere solo los elementos de un indice en cada linea, ingresar valor index diferente de -1
	## si se quiere obtener todos los valores del archivo, ingresar indice = -1

	file_readed = open(file_name, "r")
	data_array = list()

	for linea in file_readed:
		local_line = linea.strip().split(',')		## genero un array con la linea

		if(index != -1 and len(local_line) > 0):
			try:
				data_array.append( int(local_line[index]) )
			except:
				pass
		else:
			try:
				data_array.append( local_line )
			except:
				pass

	return data_array


def ask_file_name():
	file_name = str( input("ingrese nombre del archivo en crudo que desea procesar (debe tener extensión CSV:" ) )

	print("file_name 1 = " + file_name)

	return file_name

def ejec_correction_de_formato(input_file_name):
	## ejecuta script que se encarga de eliminar lineas erroneas

	len_line = 4																	## cantidad de datos separados por coma en cada linea
	corrected_file_name = input_file_name.replace(".csv", "_CORRECTED.csv")
	eliminar_errores(input_file_name, corrected_file_name, len_line)

	return(corrected_file_name)


## procesamiento de datos (reducción de ruido y otros algoritmos)
def reducir_ruido():
	##	INPUT	

	##	OUTPUT	

	print ("Ingresando a reducir_ruido()")
	auto_ejectucion_integrada()


## observación, configuración de parametros
def ejec_adaptacion_datos(input_file_name):
	##	INPUT	lee una lista de datos crudos compuesto por una fecha en timestramp, y dos valores de bateria y signal
	##	(float) Timestramp, (float) Signal, (float) Battery, (float) Variation
	print("ingresando a ejec_adaptacion_datos()")
	media_10000_name = adaptar_datos(input_file_name)
	print(str(datos[:100]) + "\nlisto...")

	##	OUTPUT	retorna una media por cada 10K datos
	##	(Date) Date, (int) Signal, (int) Battery, (int) Variation
	return media_10000_name





## visualización de grafico de FFT

	##	INPUT	

	##	OUTPUT	

def generar_archivo_procesado():


	file_name = ask_file_name()

	file_name = ejec_correction_de_formato(file_name)		## reemplaza el nombre por el del archivo corregido

	auto_ejectucion_integrada(file_name)


	media_10000_name = ejec_adaptacion_datos(file_name)


#generar_archivo_procesado()


def crear_FFT():
	## a partir del archivo generado en: generar_archivo_procesado(), se produce un grafico FFT
	file_name_FFT = str( input("ingrese nombre del grafico FFT a generar: ") )
	#axis_x_name = str( input("ingrese nombre del eje X (ej: Frecuencia (Hz): ") )
	#axis_y_name = str( input("ingrese nombre del eje Y (ej: Intensidad (mA): ") )

	## axis labels por default
	axis_x_name = "Frecuencia (Hz): "
	axis_y_name = "Intensidad (mA): "

	## abrir archivo para extraer datos
	FFT_file = str( input("ingrese nombre del archivo del cual quiere extraer datos, debe tener formato CSV: ") )
	index_data = int( input("ingrese posicion del dato (indice): ") )
	array_size = str( input("Ingrese numero de elementos que se desea graficar (dimension del array): ") )

	data_array = read_file(FFT_file, index_data)	## genero una martiz de datos, si se quiere leer archivo completo, usar index_data = -1

	print(data_array)

	generar_FFT(data_array[0:7000], file_name_FFT,axis_x_name, axis_y_name)



def cli():
	opcion = int( input("escriba 1 si desea procesar un archivo crudo, o 2 si prefiere mostrar el grafico FFT de un archivo ya proceado: ") )
	if(opcion == 1):
		generar_archivo_procesado()
	elif(opcion == 2):
		crear_FFT()
	else:
		print("Error, asegure que el dato ingresado es un numero 1 o 2")
		cli()






