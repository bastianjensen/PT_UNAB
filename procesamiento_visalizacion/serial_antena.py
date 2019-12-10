import serial
import time

arduino_data = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=3.0)

file_name = str( input("ingrese nombre del archivo que desea escribir (extension .csv): ") )

try:
    write_file = open(file_name, 'a')
except:
    write_file = open(file_name, 'w')

counter = 0
i = 0
while (True):
    try:
        this_time = time.time()
        this_data = arduino_data.readline()
        write_file.write( str(this_time) + ',' + str(this_data) )
	#write_file.write(data_line)
	#print(str(this_time) + ','+ str(this_data))
        i += 1
    except:
        pass
    
    if(i >= 10):
        counter += 1
        i = 0
        print (counter)
	#print (data_line)
        
   
    



