import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from decimal import *

import xlrd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import pandas as pd


def plot(matrix):
    
    for row in range(0, len(matrix) -1):
        print('row', matrix[row])
        x = matrix[row][0]
        y = matrix[row][1]

        scatter_plot = plt.scatter(x, y, alpha=0.5, 
                           c=x)
    
    plt.show()




def plotGraphic(matrix):
    for row in range(0, len(matrix) -1):
        previous = matrix[row]
        current = matrix[row + 1]
            
        scatter_plot = plt.scatter(previous, current, alpha=0.5, 
                           c=current)
    
    plt.show()
        


workbook = xlrd.open_workbook('./Base/S01_V01_01.xlsx')
worksheet = workbook.sheet_by_name('Accelerometer')

matrizX = []
for row in range(1, worksheet.nrows):
    newLine = []
    for col in range(18, 24):
        newLine.append(worksheet.cell(row,col).value)
    matrizX.append(newLine)

#implement PCA
pca = PCA(n_components=2)

#get the features

workbook = xlrd.open_workbook('./Base/S01_V01_01.xlsx')
worksheet = workbook.sheet_by_name('Accelerometer')
worksheet = workbook.sheet_by_index(1)
features = []
for col in range(worksheet.ncols):
    features.append(worksheet.cell(0, col).value)

# load dataset into Pandas DataFrame
df = pd.read_excel('./Base/S01_V01_01.xlsx', sheet_name='Accelerometer', names=features)

# Separating out the features
x = df.loc[:, features].values

# Standardizing the features
x = StandardScaler().fit_transform(x)
newPCA = pca.fit_transform(x)
print(len(newPCA))
print(newPCA[0])

plot(newPCA)


# pcaMatrix = []
# #Separate data corresponding to base interval
# for row in range(len(x)):
#     line = []
#     for col in range(18, 24):
#         line.append(x[row][col])
#     pcaMatrix.append(line)

# matrizY = []
# for row in range(len(matrizX)):
#     line = []
#     for principalComponent in range(len(pcaMatrix)):
#         Y = np.dot(row, principalComponent)
#         line.append(Y)
    
#     matrizY.append(line)


#plotGraphic(matrizY)




    
