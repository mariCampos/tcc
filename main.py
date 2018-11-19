import numpy as np
import csv
import pandas as pd
import decisionTree as dt
import data_imu as di

dataset_complete = []

# def get_sensor_data():


def write_clinical_database():
    print('Get the data from databse')
    dataset = pd.read_csv('./Base/Clinical_Database_last_Sheet1.csv', low_memory=False)
    dataset1 = dataset.iloc[3:28, 2:97].values.astype(float)

    dataset = pd.read_csv('./Base/Clinical_Database_last_Sheet2.csv', low_memory=False)
    dataset2 = dataset.iloc[4:29, 1:36].values.astype(float)

    #get data from IMU sensors
    ratios_from_imu = di.data_imu_main()

    for x in range(0, len(dataset1)):
        dataset_complete.append(np.concatenate((dataset1[x], dataset2[x], ratios_from_imu), axis=0))

    initialize_algorithm()


def initialize_algorithm():
    print('Initialize algorithm')
    dataset = pd.read_csv('./Base/Clinical_Database_last_Sheet1.csv', low_memory=False)
    y = np.array(dataset.iloc[3:28, 1].values.astype(int))


    dt.initialize_decision_tree(dataset_complete, y)


write_clinical_database()



