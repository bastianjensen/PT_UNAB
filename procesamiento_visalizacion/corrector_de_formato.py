

## Se encarga de asegurar que la matriz de datos tenga un formato unificado


def eliminar_errores(raw_file_name, corrected_file_name, len_line):
	## Esta funcion se encarga de asegurar que los valores almacenados cumplen con un formato estandar que podra ser leido

	raw_open_file = open(raw_file_name, "r")			## abre archivo original o crudo en modo de solo lectura
	corrected_open_file = open(corrected_file_name, "w")		## crea un archivo nuevo que tomara solo los datos validos del archivo crudo

	lineas_borradas = list()

	for linea in raw_open_file:
		array_linea = linea.strip().split(',')
		tam =  len( array_linea )

		if(tam != len_line or array_linea[0].count(".") != 1):						
		## si la cantidad de valores separados por coma es diferente a la predeterminada o si el timestrap tiene mas de un punto
			lineas_borradas.append(linea)					## se almacena la linea erronea
			continue								## vuelve a comenzar el ciclo
		corrected_open_file.write(linea)			## solo escribe las lineas que han pasado el filtro
		
	for lineab in lineas_borradas:
		print (lineab)
	return lineas_borradas


##eliminar_errores("radio_data_sun_copy.csv", "corregido.csv", 4)
    


## eliminar_errores('radio_data_sun_2.csv', 'Datos_nov_30_dic_3_DATE.csv',4)
    ## genera un archivo en que elimina datos corruptos, pero sin convertir datos