import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import lightgbm as lgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

#calculate error
def calculate_error(test, pred):
    return mean_squared_error(test, pred) 

def gbdt_params():
    params = {}
    params['learning_rate'] = 0.01
    params['boosting_type'] = 'gbdt'
    params['task'] = 'predict'
    params['application'] = 'multiclass'
    params['objective'] = 'regression_l1'
    params["bagging_freq"] = 1
    params['sub_feature'] = 0.5
    params['num_leaves'] = 31
    params['min_data'] = 1
    params['max_depth'] = 20

    return params


def rf_params():
    #random forest
    params = {}
    params['learning_rate'] = 0.01
    params['boosting_type'] = 'rf'
    params['task'] = 'predict'
    params['application'] = 'multiclass'
    params['objective'] = 'regression_l1'
    params["bagging_freq"] = 1
    params["bagging_fraction"] = 0.5
    params['sub_feature'] = 0.5
    params['num_leaves'] = 20
    params['min_data'] = 1
    params['max_depth'] = 10

    return params


def dart_params():
    # dart ( Dropouts meet Multiple Additive Regression Trees)
    params = {}
    params['learning_rate'] = 0.01
    params['boosting_type'] = 'dart'
    params['task'] = 'predict'
    params['drop_rate'] = 0.5
    params['max_drop'] = 20
    params['skip_drop'] = 0.5
    params['xgboost_dart_mode'] = False
    params['uniform_drop'] = False
    params['drop_seed'] = 1
    params['application'] = 'multiclass'
    params['objective'] = 'regression_l1'
    params["bagging_freq"] = 1
    params['sub_feature'] = 0.5
    params['num_leaves'] = 10
    params['min_data'] = 1
    params['max_depth'] = 10

    return params


def goss_params():
    # goss (Gradient-based One-Side Sampling)
    params = {}
    params['learning_rate'] = 0.01
    params['boosting_type'] = 'goss'
    params['task'] = 'predict'
    params['application'] = 'multiclass'
    params['objective'] = 'regression_l1'
    params["bagging_freq"] = 1
    params['sub_feature'] = 0.5
    params['num_leaves'] = 10
    params['min_data'] = 1
    params['max_depth'] = -1
    params['top_rate'] = 0.2
    params['other_rate'] = 0.1

    return params

#importing the dataset
# dataset = pd.read_csv('./Base/Clinical_Database_last_Sheet1.csv', low_memory=False)
# X = dataset.iloc[3:28, 2:96].values.astype(float)
# y = np.array(dataset.iloc[3:28, 1].values.astype(int))

# print('X ', X)


# Splitting the dataset into the Training set and Test set
# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


#Feature Scaling
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# x_train = sc.fit_transform(x_train)
# x_test = sc.transform(x_test)

#Using lightgbm

# d_train = lgb.Dataset(x_train, label=y_train)

# params = rf_params()
# clf = lgb.train(params, d_train, 50)

# y_pred = clf.predict(x_test)

# print('y_test', y_test)
# print('y_pred', y_pred)

# error = calculate_error(y_test, y_pred)
# print('error', error)



#Confusion matrix
#from sklearn.metrics import confusion_matrix
#cm = confusion_matrix(y_test, y_pred)
#Accuracy
#from sklearn.metrics import accuracy_score
#accuracy=accuracy_score(y_pred,y_test)
#print(accuracy)

# error = calculate_error(y_test, y_pred)
# print(error)

def initialize_decision_tree(x_data, y_data):
    
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.25, random_state = 0)

    print('y_test', y_test)

    #Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)

    #Using lightgbm

    print('initialize decision tree')

    d_train = lgb.Dataset(x_train, label=y_train)

    params = dart_params()
    clf = lgb.train(params, d_train, 50)

    y_pred = clf.predict(x_test)

    print('y_test: ', y_test)
    print('y_pred: ', y_pred)

    error = calculate_error(y_test, y_pred)
    print('Error: ', error)




