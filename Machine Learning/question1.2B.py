import pandas as pd
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt 
# %matplotlib inline
x = int (0)


cnx = mysql.connector.connect(user='ronald', password='P@ssword',
                              host='localhost',
                              database='cust_details')

if cnx.is_connected():
    print("You are connected")
else :
    print ("You are not connected")

query_4 = "Select cust_details.age, cust_details.gender, cust_details.marital_status, cust_details.nqf_level, loan_records.loan_amount, loan_records.payback_term  from cust_details inner join loan_records on cust_details.id = loan_records.id"


df_1 = pd.read_sql(query_4, cnx)
df_2 = df_1

df_2["marital_status"].replace(['married','single','divorced'],[1,-1,0],inplace= True)

from sklearn.model_selection import train_test_split

X_train, y_train,  X_test, y_test = train_test_split(X, y, test_size=0.25)
print (len(X_train))



