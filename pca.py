#Principal Component Analysis (PCA)

#Two stages of implementation

#1) Modeling the human gait
#2) --


import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns; sns.set()

import xlrd
from sklearn.decomposition import PCA

#get the features

workbook = xlrd.open_workbook('./Base/S01_V01_01.xls')
worksheet = workbook.sheet_by_name('Gyroscope')
worksheet = workbook.sheet_by_index(0)
for col in range(sheet.ncols):
    features.append(worksheet.cell(0, col).value)

#Open the table get de the values
workbook = xlrd.open_workbook('./Base/S01_V01_01.xls')
for sheet in workbook.sheets():
    for row in range(sheet.nrows):
        for column in range(sheet.ncols):
            print(sheet.cell(row,column).value)
            line.append(sheet.cell(row,column).value)
        # Separating out the features
        x = df.loc[:, features].values
    # Separating out the target
    y = df.loc[:,['target']].values
    # Standardizing the features
    x = StandardScaler().fit_transform(x)
