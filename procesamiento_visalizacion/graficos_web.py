# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
#from matplotlib import specgram
import matplotlib.pyplot as plt
import scipy.fftpack



my_data = np.loadtxt('Datos_nov_30_dic_3_MEDIA_10000.csv', comments = '#', delimiter=',')
  

time = my_data[:,0]
bateria = my_data[:,1]
bateria_mean = bateria.mean()
#bateria_mean = np.median(bateria)
bateria_norm = bateria / bateria_mean

antena = my_data[:,2]
antena_mean = antena.mean()
#antena_mean = np.median(antena)
antena_norm = antena / antena_mean


variacion =  antena - bateria ## my_data[:,3] 
variacion_mean = variacion.mean()
#variacion_mean = np.median(variacion)
variacion_norm = variacion / variacion_mean


## grafico de secuencia temporal
plt.plot(time[0:7000] - 1.571301e9, variacion[0:7000])
plt.xlabel("Secuencia temporal en segundos(s)")					##'Frecuency (KHz)'					
plt.ylabel("intensidad (mA)")					## 'Amplitude (mV)'
plt.title("Variación de intensidad versus Variación de intensidad normalizada")


plt.plot(time[0:7000] - 1.571301e9,variacion_norm[0:7000])


plt.show()



## grafico de FFT


## espectrograma

## USAR PANDAS

#my_data = np.loadtxt('radio_data_sun_copy_CORRECTED.csv', comments = '#', delimiter=',')


"""
    FFT 
"""
data = variacion_norm[0:7000]
file_name = "Variación normalizada"
N = len( data )

#print("largo de DATA:\t\t" + str(N))
#print(data[0:100])

# sample spacing
T = 1.0 / 10						## sampling interval
Fs = 1/T 							## frecuency
x = np.linspace(0.0, N*T, N)		##	
y = data[0:7000] ##[100000:100000+(number_sample_points*2)] 	## 	LEE LINEA DEL ARCHIVO ABIERTO

yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

fig, ax = plt.subplots()


ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
#plt.xlim(1,3500)#4460)					##	rango eje X
plt.ylim(0, yf.mean()/20)								##	ranfo eje y
plt.grid()									## mostrar grid en el grafico

plt.xlabel("frecuencia (Hz)")					##'Frecuency (KHz)'					
plt.ylabel("intensidad (mA)")					## 'Amplitude (mV)'
plt.title("FFT " + file_name)

plt.legend()


plt.show()
"""
x = variacion


f, t, Sxx = signal.spectrogram(x, fs)

plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
"""