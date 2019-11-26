#import pandas as pd
from datetime import datetime


##	INPUT	lee una lista de datos crudos compuesto por una fecha en timestramp, y dos valores de bateria y signal
##	(float) Timestramp, (float) Signal, (float) Battery, (float) Variation

##	OUTPUT	retorna una media por cada 10K datos
##	(Date) Date, (int) Signal, (int) Battery, (int) Variation




def adaptar_datos(input_file_name):

	## nombre del archivo a leer
	file_name = str(input_file_name)												## nombre ingresado por consola


	new_file = file_name.replace(".csv", "_CONVERTED_TO_DATE.csv")

	media_file_10000_name = file_name.replace(".csv", "_MEDIA_10000.csv")	## media por cada 10.000 datos
	media_file_10000 = open(media_file_10000_name, "w")
	local_battery = 0
	local_signal = 0
	local_variation = 0
	media_range = 10000


	## Lectura de archivo

	#print("el nombre de archivo es: " + file_name)
	data = open(file_name, "r")
	converted_to_date_file = open( new_file, "w")

	i = 0
	## Conversión de timestramp a date
	for line in data:

		try:
			local_line = data.readline().split(',')								## crea una lista, separa los valores de fecha y signal
			#local_line[3] = int(local_line[1]) + int(local_line[2])
			local_line[0] =  float(local_line[0])
			local_line[0] = datetime.fromtimestamp( local_line[0]) 		## convierte el valor timetramp de string a float, y de timestramp a date
			local_line[0] = str(local_line[0])									## vuelve a convertir el valor a un string
			local_line[3] =  str( int(local_line[2])-int(local_line[1]) )
			
			
			## inicio prueba
			local_battery += int(local_line[1])
			local_signal += int(local_line[2])
			local_variation += int(local_line[3])
			date = local_line[0]
			## fin prueba
			

			local_line = str(local_line)										## convierte la lista en string
			local_line = local_line + "\n"										## agrega salto de linea
			local_line = local_line.replace("'","")								## elimina las comillas generadas en la conversion a string
			local_line = local_line[:24] + local_line[27:].replace(" ","")								## elimina espacios
			local_line = local_line[1:-2]										## elimina los parentecis cuadrados generados en la conversion a string
			#local_line[0] = local_line[11:-2]


			## Se escribe archivo "_CONVERTED_TO_DATE"
			converted_to_date_file.write(local_line + "\n")	

			
			## Se escribe archivo "MEDIA_FILE_10000"

			i += 1
			if(i >= media_range):
				i = 0
				media_file_10000.write( date + "," + str(round(local_battery/media_range)) + "," + str(round(local_signal/media_range)) + "," + str(round(local_variation/media_range)) + "\n" )
				local_battery = 0
				local_signal = 0
				local_variation = 0
			

		except:
			pass
	print("Datos enviados desde el modulo: adaptacion_datos_0_8")
	return (media_file_10000_name)	## retorna el nombre del archivo creado

##adaptar_datos("radio_data_sun_copy.csv")


print("OK:	Los datos han sido transformados desde un archivo crudo a un archivo procesable")