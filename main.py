import numpy as np
import csv
import pandas as pd
import decisionTree as dt
import data_imu as di

dataset_complete = []

# def get_sensor_data():


def write_clinical_database():
    print('Get the data from databse')
    dataset = pd.read_csv('./Base/Clinical_Database_45_Sheet1.csv', low_memory=False)
    dataset1 = dataset.iloc[3:48, 2:97].values.astype(float)

    dataset = pd.read_csv('./Base/Clinical_Database_45_Sheet2.csv', low_memory=False)
    dataset2 = dataset.iloc[4:49, 1:36].values.astype(float)

    #get data from IMU sensors
    # ratios_from_imu = di.data_imu_main()
    # print('Ratios rom IMU', ratios_from_imu)

    for x in range(0, len(dataset1)):
        dataset_complete.append(np.concatenate((dataset1[x], dataset2[x]), axis=0))

    initialize_algorithm()


def initialize_algorithm():
    print('Initialize algorithm')
    dataset = pd.read_csv('./Base/Clinical_Database_45_Sheet1.csv', low_memory=False, delimiter=",")
    y = np.array(dataset.iloc[3:48, 1].values.astype(int))

    print("AQUIIIIIIIIIIIIIIIIIIIII \n", y)


    dt.initialize_decision_tree(dataset_complete, y)


write_clinical_database()



