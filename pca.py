#Principal Component Analysis (PCA)

#Two stages of implementation

#1) Modeling the human gait
#2) --


import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns; sns.set()

import xlrd
from sklearn.decomposition import PCA

#Open the table get de the values

# workbook = xlrd.open_workbook('./Base/S01_V01_01.xls')
# worksheet = workbook.sheet_by_name('Gyroscope')
# worksheet = workbook.sheet_by_index(0)
# print(worksheet.cell(1, 0).value)

workbook = xlrd.open_workbook('./Base/S01_V01_01.xls')
for sheet in workbook.sheets():
    for row in range(sheet.ncols):
        for column in range(sheet.ncols):
            print(sheet.cell(row,column).value)
