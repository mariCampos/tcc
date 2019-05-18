import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import lightgbm as lgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

#calculate error
def calculate_error(test, pred):
    return mean_squared_error(test, pred) 

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def gbdt_params():
    params = {}
    params['learning_rate'] = 0.01
    params['boosting_type'] = 'gbdt'
    params['task'] = 'predict'
    params['application'] = 'regression'
    params['objective'] = 'regression_l2'
    params["bagging_freq"] = 1
    params['sub_feature'] = 0.5
    params['num_leaves'] = 31
    params['num_iterations'] = 1000
    params['min_data'] = 1
    params['max_depth'] = 20
    params['metric'] = 'binary_logloss'
    params['input_model'] = 'predict'

    return params


def rf_params():
    #random forest
    params = {}
    params['learning_rate'] = 0.1
    params['boosting_type'] = 'rf'
    params['task'] = 'predict'
    params['application'] = 'regression'
    params['objective'] = 'regression_l2'
    params["bagging_freq"] = 1
    params["bagging_fraction"] = 0.5
    params['sub_feature'] = 0.5
    params['num_leaves'] = 900
    params['min_data'] = 1
    params['max_depth'] = 15
    params['num_iterations'] = 700
    params['n_estimators'] = 300
    params['colsample_bytree'] = 0.7
    params['n_jobs'] = 1
    params['reg_lambda'] = 0

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
    params['objective'] = 'regression_l2'
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
    params['application'] = 'regression'
    params['objective'] = 'regression_l2'
    params["bagging_freq"] = 1
    params['sub_feature'] = 0.5
    params['num_leaves'] = 20
    params['min_data'] = 1
    params['max_depth'] = -1
    params['num_iterations'] = 1000
    params['top_rate'] = 0.2
    params['other_rate'] = 0.1


    return params

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

    params = rf_params()
    clf = lgb.train(params, d_train, 50)

    y_pred = clf.predict(x_test)

    print("Random Forest test \n")

    print('y_test: ', y_test)
    print('y_pred: ', y_pred)

    print(" =================== METRICS ===================")

    error = calculate_error(y_test, y_pred)
    print('Error: ', error)

    from sklearn.metrics import explained_variance_score
    explained_variance = explained_variance_score(y_test, y_pred)
    print("Explained variance: ", explained_variance)

    mean_absolute_error = mean_absolute_percentage_error(y_test, y_pred)
    print("Mean Absolute Percentage error: ", mean_absolute_error, "%")

