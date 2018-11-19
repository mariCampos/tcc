import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from scipy import signal
from scipy.signal import butter, lfilter
from scipy.ndimage.filters import gaussian_filter
from decimal import *

import xlrd

params = {}

all_ratios_array = []


def plot(time, data_left, data_right):
    plt.figure()
    inflection_left = get_max_min(data_left)
    plt.plot(time, data_left, '-gD', markevery=inflection_left)
    plt.show()

    plt.figure()
    inflection_right = get_max_min(data_right)
    plt.plot(time, data_right, '-rD', markevery=inflection_right)
    plt.show()

    get_time(time, inflection_left, inflection_right)



def gaussian_smooth(x):
    return gaussian_filter(x, 10)

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=20):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y



def get_max_min(data):
    array = []
    for x in range(0, len(data) -1):
        previous = data[x-1]
        
        if (data[x] > previous and data[x] > data[x+1]) or (data[x] < previous and data[x] < data[x+1]):
            array.append(x)
    
    return array

def get_time(time, markers_left, markers_right):

    ec_1 = time[markers_left[18]]
    ic_2 = time[markers_left[20]]
    ec_2 = time[markers_left[22]]

    t_sw = ic_2 - ec_1
    t_st = ec_2 - ic_2

    params['t_sw_l'] = round(t_sw, 2)
    params['t_st_l'] = round(t_st, 2)

    ec_1 = time[markers_right[18]]
    ic_2 = time[markers_right[20]]
    ec_2 = time[markers_right[22]]

    t_sw = ic_2 - ec_1
    t_st = ec_2 - ic_2

    params['t_sw_r'] = round(t_sw, 2)
    params['t_st_r'] = round(t_st, 2)

    print(params)

    calculate_ratios()

    

def calculate_ratios():
    t_st_r = params.get('t_st_r')
    t_st_l = params.get('t_st_l')

    print('t_st_r', t_st_r)
    print('t_st_l', t_st_l)
    params['r_st'] = round((t_st_r / t_st_l), 2)
    all_ratios_array.append(round((t_st_r / t_st_l), 2))

    t_sw_r = params.get('t_sw_r')
    t_sw_l = params.get('t_sw_l')

    params['r_sw'] = round((t_sw_r / t_sw_l), 2)
    all_ratios_array.append(round((t_sw_r / t_sw_l), 2))

    print(params)

    return params


def get_imu_data_from_shank(worksheet):
    workbook = xlrd.open_workbook('./Base/S01_V02_01.xlsx')
    worksheet = workbook.sheet_by_name('Accelerometer')

    total_time = worksheet.nrows / 100
    interval = total_time / worksheet.nrows
    time = 0.0

    array_time = []
    array_data_left = []
    array_data_right = []

    #left sensor
    for row in range(1, worksheet.nrows):
        for col in range(15,16):
            array_data_left.append(worksheet.cell(row,col).value)
            array_time.append(time)
            time = round(time + interval, 2)

    array_time = []

    #right sensor
    for row in range(1, worksheet.nrows):
        for col in range(18,19):
            array_data_right.append(worksheet.cell(row,col).value)
            array_time.append(time)
            time = round(time + interval, 2)

    #get gaussian
    array_data_left = gaussian_smooth(array_data_left)
    array_data_right = gaussian_smooth(array_data_right)

    #get low pass filter with cut off
    #array_data = butter_lowpass_filter(array_data, 8, 100, order=10)

    #plot the array the gaussian curve
    plot(array_time, array_data_left, array_data_right)



def get_imu_data_from_footer(worksheet):

    total_time = worksheet.nrows / 100
    interval = total_time / worksheet.nrows
    time = 0.0

    array_time = []
    array_data_left = []
    array_data_right = []

    #left sensor
    for row in range(1, worksheet.nrows):
        for col in range(20,21):
            array_data_left.append(worksheet.cell(row,col).value)
            array_time.append(time)
            time = round(time + interval, 2)

    array_time = []

    #right sensor
    for row in range(1, worksheet.nrows):
        for col in range(23,24):
            array_data_right.append(worksheet.cell(row,col).value)
            array_time.append(time)
            time = round(time + interval, 2)

    #get gaussian
    array_data_left = gaussian_smooth(array_data_left)
    array_data_right = gaussian_smooth(array_data_right)

    #get low pass filter with cut off
    #array_data = butter_lowpass_filter(array_data, 8, 100, order=10)

    #plot the array the gaussian curve
    plot(array_time, array_data_left, array_data_right)


def get_imu_data_from_hand(worksheet):

    total_time = worksheet.nrows / 100
    interval = total_time / worksheet.nrows
    time = 0.0

    array_time = []
    array_data_left = []
    array_data_right = []

    #left sensor
    for row in range(1, worksheet.nrows):
        for col in range(6,7):
            array_data_left.append(worksheet.cell(row,col).value)
            array_time.append(time)
            time = round(time + interval, 2)

    array_time = []

    #right sensor
    for row in range(1, worksheet.nrows):
        for col in range(9,10):
            array_data_right.append(worksheet.cell(row,col).value)
            array_time.append(time)
            time = round(time + interval, 2)

    #get gaussian
    array_data_left = gaussian_smooth(array_data_left)
    array_data_right = gaussian_smooth(array_data_right)

    #get low pass filter with cut off
    #array_data = butter_lowpass_filter(array_data, 8, 100, order=10)

    #plot the array the gaussian curve
    plot(array_time, array_data_left, array_data_right)

def data_imu_main():

    print('Initialize IMU script')
    for i in range(2,3):
        for j in range(1,5):
            workbook = xlrd.open_workbook('./Base/S01_V0' + str(i) + '_0'+ str(j) +'.xlsx')
            worksheet = workbook.sheet_by_name('Accelerometer')

            get_imu_data_from_footer(worksheet)

            get_imu_data_from_shank(worksheet)

            get_imu_data_from_hand(worksheet)

    return all_ratios_array






# workbook = xlrd.open_workbook('./Base/S01_V02_01.xlsx')
# worksheet = workbook.sheet_by_name('Accelerometer')

# total_time = worksheet.nrows / 100
# interval = total_time / worksheet.nrows
# time = 0.0

# array_time = []
# array_data_left = []
# array_data_right = []

# #left sensor
# for row in range(1, worksheet.nrows):
#     for col in range(20,21):
#         array_data_left.append(worksheet.cell(row,col).value)
#         array_time.append(time)
#         time = round(time + interval, 2)

# array_time = []

# #right sensor
# for row in range(1, worksheet.nrows):
#     for col in range(23,24):
#         array_data_right.append(worksheet.cell(row,col).value)
#         array_time.append(time)
#         time = round(time + interval, 2)

# #get gaussian
# array_data_left = gaussian_smooth(array_data_left)
# array_data_right = gaussian_smooth(array_data_right)

# #get low pass filter with cut off
# #array_data = butter_lowpass_filter(array_data, 8, 100, order=10)

# #plot the array the gaussian curve
# plot(array_time, array_data_left, array_data_right)




