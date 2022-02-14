# -*- coding: utf-8 -*-
"""


@author: Jeison Robles Arias
"""

#Import some data analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import sqlite3

#Create a conection to data base

Conn = sqlite3.connect('C:\Jeison\Python\MALL_CUSTOMERS\Mall_Customers.db')

#Import Tables from SQL and store it in DataFrames

Mall_Customers = pd.read_sql_query('SELECT * FROM Mall_Customers', Conn)

print(Mall_Customers.shape)

print(Mall_Customers.isnull().sum())

print(Mall_Customers.info())

print(Mall_Customers.head())

X = Mall_Customers.iloc[:,[3,4]].values

print (X.shape)



from sklearn.cluster import KMeans
wcss = []


for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    


plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('wcss')
plt.show()



