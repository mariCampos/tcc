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
    plt.plot(time, data)
    plt.show()


def gaussian_smooth(x):
    return gaussian_filter(x, 15)

def get_inflection_point(data):
    dx = np.diff(data)
    dx2 = np.diff(dx)
    return dx2
    #return np.sum(dx[1:] * dx[:-1] < 0)




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
print(get_inflection_point(array_data))
plot(array_time, array_data)
