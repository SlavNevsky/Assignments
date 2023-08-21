from locale import normalize
import pandas as pd
import mysql.connector
import os
import numpy as np
single = -1
divorced = 0 
married = 1


cnx = mysql.connector.connect(user='ronald', password='P@ssword',
                              host='localhost',
                              database='cust_details')

if cnx .is_connected():
    print("You are connected")
else :
    print ("You are not connected")

query1 = "SELECT marital_status from cust_details"
query_4 = "Select cust_details.age, cust_details.gender, cust_details.marital_status, cust_details.nqf_level, loan_records.loan_amount, loan_records.payback_term  from cust_details inner join loan_records on cust_details.id = loan_records.id"


df_1 = pd.read_sql(query_4, cnx)
df_2 = df_1

df_2["marital_status"].replace(['married','single','divorced'],[1,-1,0],inplace= True)


# def normMax (column):
#     return (column/column.max())


df_2["marital_status"] = df_2["marital_status"]/df_2["marital_status"].max()
df_2["age"] = df_2["age"]/df_2["age"].max()
df_2["nqf_level"] = df_2["nqf_level"]/df_2["nqf_level"].max()

print (df_2)




