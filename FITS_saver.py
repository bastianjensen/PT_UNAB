## Generar tablas de datos estructurados

from astropy.table import Table


##CODIGO EJEMPLO

"""
names = ['M31', 'NGC1232', 'M81']
magnitudes = [3.4, 9.9, 6.9]

tabla = Table([names, magnitudes], names= ('name', 'mag'),
	meta ={'name': 'Lista de galaxias'})


## Guardar archivo FITS
tabla.write("tabla.fits")



print( tabla['name'] )
=>	 	name 
		-------
    		M31
		NGC1232
    		M81

print( tabla['mag'].data ) 
=> 		[3.4 9.9 6.9]

print ( tabla )
=>		  name  mag
		------- ---
		    M31 3.4
		NGC1232 9.9
		    M81 6.9
"""



