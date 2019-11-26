import pandas as pd
from datetime import datetime


## nombre del archivo a leer
file_name = "radio_data_sun.csv"
new_file = file_name.replace(".csv", "_CONVERTED_TO_DATE.csv")


## Lectura de archivo
data = open(file_name, "r")
converted_to_date_file = open( new_file, "w")

i = 0
## Conversión de timestramp a date
for line in data:
	local_line = data.readline().split(',')								## crea una lista, separa los valores de fecha y signal
	#local_line[3] = int(local_line[1]) + int(local_line[2])
	local_line[0] = datetime.fromtimestamp(float(local_line[0]))		## convierte el valor timetramp de string a float, y de timestramp a date
	local_line[0] = str(local_line[0])									## vuelve a convertir el valor a un string
	local_line[3] =  str( int(local_line[2])-int(local_line[1]) )
	local_line = str(local_line)										## convierte la lista en string
	local_line = local_line + "\n"										## agrega salto de linea
	local_line = local_line.replace("'","")								## elimina las comillas generadas en la conversion a string
	local_line = local_line[:24] + local_line[27:].replace(" ","")								## elimina espacios
	local_line = local_line[1:-2]										## elimina los parentecis cuadrados generados en la conversion a string
	#local_line[0] = local_line[11:-2]


	converted_to_date_file.write(local_line + "\n")

	i += 1
	if(i%1000 == 0):
		print(i)


print("FIN...")