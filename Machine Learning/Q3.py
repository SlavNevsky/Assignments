import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import preprocessing 
from sklearn.linear_model import LinearRegression
from  sklearn.model_selection import train_test_split

df = pd.read_csv('merka_agri_corn_experiment.csv')

x_plt = df[['fertilizer_addition']]
y_plt = df[['corn_weight']]

plt.scatter (x_plt,y_plt, color = 'purple')
plt.xlabel('fertilizer_addition')
# naming the y axis
plt.ylabel('corn_weight')

# giving a title to my graph
plt.title('Fertilizer Addition vs Corn Weight')

# function to show the plot
plt.show()

#Question 3.2
X = df[['fertilizer_addition']]
y = df[['corn_weight']]

X_train, X_test, y_train , y_test = train_test_split(X,y, train_size=0.99)


regr = LinearRegression()
regr.fit(X_train,y_train)

print(regr.score(X_train,y_train))

y_pred = regr.predict(X_train)


plt.scatter (X_train,y_pred, color = 'orange')
plt.xlabel ('fertilizer_addition')
plt.ylabel ('corn_weight')
plt.title ('Regressed Data of Fertillizer Addition vs Corn Weight')
plt.show()

print ("The Coefficient or Gradient or a : ", regr.coef_)
print (" Intercept or b : ", regr.intercept_)

print ("weight = ",regr.coef_,"* fertilizer_addition + ", regr.intercept_)

#Question 3.3
import pylab
  
pylab.scatter (x_plt, y_plt, color = 'purple', label = 'Non-regressed')
pylab.scatter (X_train, y_pred, color = 'red', label ='Regressed')
pylab.xlabel ('fertilizer_addition')
pylab.ylabel ('corn_weight')
pylab.title ('Regressed Data vs Non-Regressed Data')
pylab.legend( )
pylab.show()

#Question 3.4

weight = (regr.coef_*50 + regr.intercept_)
print ("The weight of the corn will be : ", weight)
