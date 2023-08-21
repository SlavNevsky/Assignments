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


#Question 3.1
df = pd.read_csv("gambi_choco_research.csv")

X_plt = df[["gram"]]
y_plt = df[["price"]]

plt.scatter (X_plt,y_plt, color = 'purple')
plt.xlabel('Gram')
# naming the y axis
plt.ylabel('Price')

# giving a title to my graph
plt.title('Grams vs Price')

# function to show the plot
plt.show()

#Question 3.2

X_train1 = df[['gram']]
y_train1 = df[['price']]


regr = LinearRegression()
regr.fit(X_train1,y_train1)

print(regr.score(X_train1,y_train1))

y_pred = regr.predict(X_train1)


plt.scatter (X_train1,y_pred, color = 'orange')
plt.xlabel ('Gram')
plt.ylabel ('Price')
plt.title ('Regressed Data of Gram vs Price')
plt.show()

print ("The Coefficient or Gradient or a : ", regr.coef_)
print ("Intercept or b : ", regr.intercept_)

print ("milk_price = ",regr.coef_,"* can_weight + ", regr.intercept_)

#Question 3.3

import pylab
  
pylab.scatter (X_plt, y_plt, color = 'purple', label = 'Non-regressed')
pylab.scatter (X_train1, y_pred, color = 'red', label ='Regressed')
pylab.xlabel ('Gram')
pylab.ylabel ('Price')
pylab.title ('Regressed Data vs Non-Regressed Data')
pylab.legend( )
pylab.show()

#Question 3.4
score = r2_score(y_pred, y_train1)
print(" The coefficient =  ", score, "\n")


#Question 4.1
df1 = pd.read_csv("OLART_customers.csv")
df1 = df1.dropna()

X_plt1 = df1[["Annual Income (k$)"]]
y_plt1 = df1[["Spending Score (1-100)"]]

plt.scatter (X_plt1,y_plt1, color = 'red')
plt.xlabel('Annual Income')
# naming the y axis
plt.ylabel('Spending Score')

# giving a title to my graph
plt.title('Annual Income vs Spending Score')

# function to show the plot
plt.show()


#Question 4.2

from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

df2 = df1.drop (columns=['Genre'])


sv = []
for i in range (2,15):
    kmeans = KMeans(i)
    kmeans.fit(df2)
    score1 = silhouette_score(df2, kmeans.labels_, metric = 'euclidean')
    sv.append(score1)

plt.figure()
plt.plot(np.arange(2,15),sv)
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette')
plt.xticks(range(2,15))
plt.title('Silhouette Method')
plt.show()

#Question 4.3
kmeans = KMeans(2)
clusterIds = kmeans.fit_predict(df2)
df2['clusters'] = clusterIds
x = df2['Annual Income (k$)']
y = df2['Spending Score (1-100)']
plt.figure()
plt.xlabel(df2.columns[2])
plt.ylabel(df2.columns[3])
plt.scatter(x,y,c=df2['clusters'])
plt.title('Clustering datasets')
plt.show()



