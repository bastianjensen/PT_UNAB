import pandas as pd
from datetime import datetime


## nombre del archivo a leer
file_name = "radio_data_sun.csv"
new_file = file_name.replace(".csv", "_CONVERTED_TO_DATE.csv")

media_file_10000_name = file_name.replace(".csv", "_MEDIA_10000.csv")	## media por cada 10.000 datos
media_file_10000 = open(media_file_10000_name, "w")
local_media_1 = 0
local_media_2 = 0
local_media_3 = 0
media_range = 10000


## Lectura de archivo
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
		bateria_media += int(local_line[1])
		senal_media += int(local_line[2])
		variacion_media += int(local_line[3])
		date = local_line[0]
		## fin prueba
		

		local_line = str(local_line)										## convierte la lista en string
		local_line = local_line + "\n"										## agrega salto de linea
		local_line = local_line.replace("'","")								## elimina las comillas generadas en la conversion a string
		local_line = local_line[:24] + local_line[27:].replace(" ","")								## elimina espacios
		local_line = local_line[1:-2]										## elimina los parentecis cuadrados generados en la conversion a string
		#local_line[0] = local_line[11:-2]


		converted_to_date_file.write(local_line + "\n")

		
		i += 1
		if(i >= media_range):
			i = 0
			media_file_10000.write( date + "," + str(bateria_media/media_range) + "," + str(senal_media/media_range) + "," + str(variacion_media/media_range) + "\n" )
			bateria_media = 0
			senal_media = 0
			variacion_media = 0
		

	except:
		pass


print("FIN...")