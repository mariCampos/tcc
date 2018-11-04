import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
from scipy import signal
from scipy.ndimage.filters import gaussian_filter
from decimal import *

import xlrd

def plot(time, data):
    plt.figure()
    inflection = get_max_min(data)
    plt.plot(time, data, '-gD', markevery=inflection)
    plt.show()


def gaussian_smooth(x):
    return gaussian_filter(x, 15)


def get_max_min(data):
    array = []
    for x in range(0, len(data) -1):
        previous = data[x-1]
        
        if (data[x] > previous and data[x] > data[x+1]) or (data[x] < previous and data[x] < data[x+1]):
            array.append(x)
    
    return array



workbook = xlrd.open_workbook('./Base/S01_V02_01.xlsx')
worksheet = workbook.sheet_by_name('Accelerometer')

total_time = worksheet.nrows / 100
interval = total_time / worksheet.nrows
time = 0.0

array_time = []
array_data = []
for row in range(1, worksheet.nrows):
    for col in range(18,19):
        array_data.append(worksheet.cell(row,col).value)
        array_time.append(time)
        time = round(time + interval, 2)

#get gaussian
array_data = gaussian_smooth(array_data)

#plot the array the gaussian curve
#plot(array_time, array_data)

#Get the diff
plot(array_time, array_data)
