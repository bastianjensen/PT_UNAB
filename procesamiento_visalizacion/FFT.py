#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:08:52 2019

@author: bastianjensen
"""


# Python example - Fourier transform using numpy.fft method

import numpy as np
import matplotlib.pyplot as plotter
import pandas as pd

 
url = 'https://raw.githubusercontent.com/bastianjensen/PT_UNAB/procesamiento/procesamiento_visalizacion/Datos_nov_30_dic_3_MEDIA_10000.csv'


df = pd.read_csv(url)   ## lee un archivo CSV de github

print(df.head(5))       ## imprime las primeras X lineas
## obtener fila = var_name.get("header")




# How many time points are needed i,e., Sampling Frequency

samplingFrequency   = 10;

 

# At what intervals time points are sampled

samplingInterval       = 1 / samplingFrequency;

 

# Begin time period of the signals

beginTime           = 0;

 

# End time period of the signals

endTime             = 10; 


 

# Time points

time        = np.arange(beginTime, endTime, samplingInterval);


 

# Create subplot

figure, axis = plotter.subplots(2, 1)

plotter.subplots_adjust(hspace=1)

 


 

# Add the sine waves

lista = list( df['variation'] )

amplitude = lista

 
"""
# Time domain representation of the resultant sine wave

axis[2].set_title('Sine wave with multiple frequencies')

axis[2].plot(time, amplitude)

axis[2].set_xlabel('Time')

axis[2].set_ylabel('Amplitude')
"""
 

# Frequency domain representation

fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude

fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency

 

tpCount     = len(amplitude)

values      = np.arange(int(tpCount/2))

timePeriod  = tpCount/samplingFrequency

frequencies = values/timePeriod

 

# Frequency domain representation

axis[3].set_title('Fourier transform depicting the frequency components')

 

axis[3].plot(frequencies, abs(fourierTransform))

axis[3].set_xlabel('Frequency')

axis[3].set_ylabel('Amplitude')

 

plotter.show()