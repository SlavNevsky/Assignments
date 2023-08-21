import pandas as pd
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neural_network import MLPRegressor
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


#Question 2.1
df = pd.read_csv('Prek_HR_data.csv')
X = df[['nqf', 'age', 'exp_level']]
y = df[['q_score']]

X_train, X_test, y_train , y_test = train_test_split(X,y, test_size=0.15)

#Question 2.2
dtc = DecisionTreeClassifier()

dtc = dtc.fit(X_train,y_train)

y_pred = dtc.predict (X_test)
y_pred2 = dtc.predict (X_train)

print ("Accuracy Test : ", metrics.accuracy_score(y_test, y_pred))
print ("Accuracy Train : ", metrics.accuracy_score(y_train, y_pred2))


# from sklearn.tree import export_graphviz
# from IPython.display import Image
# import pydotplus
# import six
# import sys
# sys.modules['sklearn.externals.six'] = six
# from six import StringIO
# import os

df_2 = pd.read_csv('Q2_3_data.csv')
X_2 = df_2[['nqf', 'age', 'exp_level']]
y_2 = df_2[['q_score']]

print (len(X_2))
print (X_2)

y_pred3 = dtc.predict(X_2)

print ("Prediction :", "\n", y_pred3 )


