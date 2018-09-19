#Principal Component Analysis (PCA)

#Two stages of implementation

#1) Modeling the human gait
#2) --


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#import seaborn as sns; sns.set()

import xlrd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import pandas as pd


def plotGraphic(matrix):
    for row in range(0, len(matrix) -1):
        previous = matrix[row]
        current = matrix[row + 1]
            
        scatter_plot = plt.scatter(previous, current, alpha=0.5, 
                           c=current)
    
    plt.show()
        


'''
matrizY = []
for vel in range(1,5):
    for coleta in range(1,5):

        #get the features
        workbook = xlrd.open_workbook('./Base/S01_V0' + str(vel) + '_0' + str(coleta) + '.xlsx')
        worksheet = workbook.sheet_by_name('Gyroscope')
        features = []
        for col in range(worksheet.ncols):
            features.append(worksheet.cell(0, col).value)
        
        #Open the table get de the values
        workbook = pd.read_excel('./Base/S01_V0' + str(vel) + '_0' + str(coleta) + '.xlsx', sheet_name='Gyroscope')
        # Separating out the features
        x = workbook.loc[:, features].values
        # Standardizing the features
        standard = StandardScaler().fit_transform(x)
        pca = PCA(n_components=24)

        #Calculate pca
        principalComponents = pca.fit_transform(standard)

        #get each line and calculate dot product with the pca
        workbook = xlrd.open_workbook('./Base/S01_V0' + str(vel) + '_0' + str(coleta) + '.xlsx')
        worksheet = workbook.sheet_by_name('Gyroscope')

        
        for row in range(1, worksheet.nrows):
            lineMatriz = []
            line = []
            for column in range(worksheet.ncols):
                # print(worksheet.cell(row,column).value)
                line.append(worksheet.cell(row,column).value)
            
            newLine = np.asarray(line, dtype=np.float32)

            for pcaArray in principalComponents:
                Y = np.dot(newLine, pcaArray)
                lineMatriz.append(Y)

            matrizY.append(lineMatriz)


print(matrizY)
        #The second stage




'''
#get the features

workbook = xlrd.open_workbook('./Base/S01_V01_01.xlsx')
worksheet = workbook.sheet_by_name('Gyroscope')
worksheet = workbook.sheet_by_index(0)
features = []
for col in range(worksheet.ncols):
    features.append(worksheet.cell(0, col).value)

#Open the table get de the values
workbook = pd.read_excel('./Base/S01_V01_01.xlsx', sheet_name='Gyroscope')
# Separating out the features
x = workbook.loc[:, features].values

pca = PCA(n_components=24)

# #Calculate pca
principalComponents = pca.fit(np.array(x))
print('pca', principalComponents.singular_values_)

#get each line and calculate dot product with the pca
workbook = xlrd.open_workbook('./Base/S01_V01_01.xlsx')
worksheet = workbook.sheet_by_index(0)

matrizY = []
for row in range(1, worksheet.nrows):
    line = []
    lineMatriz = []
    for column in range(worksheet.ncols):
        line.append(worksheet.cell(row,column).value)
    
    newLine = np.asarray(line, dtype=np.float32)
    Y = np.dot(newLine, principalComponents.singular_values_)
    lineMatriz.append(Y)

    matrizY.append(lineMatriz)

plotGraphic(matrizY)


#The second stage

    
