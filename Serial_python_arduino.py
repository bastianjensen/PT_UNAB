import serial
import time


##serial.Serial('/dev/cu.usbmodem14201',11500, timeout=1)
a = serial.Serial('/dev/cu.usbmodem14201',115200)

file_input = str(input("nombre del archivo nuevo sin extención: ") + ".csv")
times = int(input("cantidad de datos grabados: "))

new_file = open(file_input, "w")

counter = 0
while counter < times:
	new_file.write(str(a.readline().split()[0])[2:-1]+"\n")
	counter += 1




