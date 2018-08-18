#Principal Component Analysis (PCA)

#Two stages of implementation

#1) Modeling the human gait
#2) --


import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns; sns.set()

import xlrd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import pandas as pd

#get the features

workbook = xlrd.open_workbook('./Base/S01_V01_01.xls')
worksheet = workbook.sheet_by_name('Gyroscope')
worksheet = workbook.sheet_by_index(0)
features = []
for col in range(worksheet.ncols):
    features.append(worksheet.cell(0, col).value)

#Open the table get de the values
workbook = pd.read_excel('./Base/S01_V01_01.xls', sheetname='Gyroscope')
# Separating out the features
x = workbook.loc[:, features].values
# Standardizing the features
standard = StandardScaler().fit_transform(x)
pca = PCA(n_components=24)

#Calculate pca
principalComponents = pca.fit_transform(standard)
print('principalComponents', principalComponents)
#get each line and calculate dot product with the pca
workbook = xlrd.open_workbook('./Base/S01_V01_01.xls')
worksheet = workbook.sheet_by_index(0)
for row in range(1, worksheet.nrows):
    line = []
    for column in range(worksheet.ncols):
        # print(worksheet.cell(row,column).value)
        line.append(worksheet.cell(row,column).value)
    
    newLine = np.asarray(line, dtype=np.float32)
    Y = np.dot(newLine, principalComponents[0])
    #print(Y)


#The second stage


    
