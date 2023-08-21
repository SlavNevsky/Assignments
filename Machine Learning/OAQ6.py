import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import preprocessing 
from sklearn.linear_model import LinearRegression
from  sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LogisticRegression



#Question 6.1

df = pd.read_csv("pavland_cleveland_datasets.csv")


df = df.replace(['?'],[0])

df = df.dropna()

X = df[['age','sex','cp','threstbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']]
y = df[['num']]

#Question 6.2

X_train, X_test, y_train , y_test = train_test_split(X,y, test_size=0.2)

model = LogisticRegression()
model.fit (X_train,y_train)

y_pred=model.predict(X_test)
print("The Score with Tested : ", (r2_score(y_pred, y_test)))

y_pred2 = model.predict(X_train)
print ("The Score with Trained : ", (r2_score(y_pred2, y_train)))


#Question 6.3
from sklearn.metrics import confusion_matrix
cm_train = confusion_matrix(y_pred2,y_train)
cm_test = confusion_matrix(y_pred,y_test)
print("Train Confusion matrix", cm_train)
print("Test Confusion Matrix",cm_test)


from sklearn.metrics import accuracy_score

print ("Accuracy Score for Train Data : ", accuracy_score(y_pred2,y_train), "\n")

print("Accuracy Score for Test Data : ", accuracy_score(y_pred, y_test))


