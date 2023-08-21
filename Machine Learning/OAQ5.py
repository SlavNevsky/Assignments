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


#Question 5.1
df = pd.read_csv("np_regression_dataset2.csv")

X_plt = df[["x"]]
y_plt = df[["y"]]

plt.scatter (X_plt,y_plt, color = 'purple')
plt.xlabel('X')
# naming the y axis
plt.ylabel('Y')

# giving a title to my graph
plt.title('X vs Y')

# function to show the plot
plt.show()

#Question 5.2

X = df[['x']]
y = df[['y']]

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler (feature_range = (-1,1))
scaler.fit(X)
X_scaled = scaler.fit_transform(X)

print ( X_scaled)


mlp = MLPRegressor(hidden_layer_sizes= (100,100), activation='relu', solver='adam', max_iter=1000).fit(X_scaled, y)

y_pred = mlp.predict(X_scaled)
print ("The Score with Trained : ", (r2_score(y_pred, y)))


#Question 5.3

X_plt1 = X_scaled
y_plt1 = df[["y"]]

plt.scatter (X_plt1,y_plt1, color = 'orange')
plt.scatter (X_plt,y_plt, color = 'purple')
plt.xlabel('X Scaled')
# naming the y axis
plt.ylabel('Y')

# giving a title to my graph
plt.title('X-Scaled vs Y')

# function to show the plot
plt.show()

#Question 5.4

import seaborn as sn
sn.lineplot(x="x",y="y", data=df)
plt.show()

