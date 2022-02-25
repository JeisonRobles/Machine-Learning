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

Mall_Customers_1 = Mall_Customers.iloc[:,[2,3,4]]


print(Mall_Customers_1.corr('pearson'))

print(Mall_Customers_1.shape)

print(Mall_Customers.shape)

print(Mall_Customers.isnull().sum())

print(Mall_Customers.info())

print(Mall_Customers.head())

X = Mall_Customers.iloc[:,[3,4]].values
X_1 = Mall_Customers.iloc[:,[2,4]]

#Lets take a look of a general distribution plotting

x = Mall_Customers.iloc[:,[3]].values
y = Mall_Customers.iloc[:,[4]].values
a = Mall_Customers.iloc[:,[2]].values


sns.pairplot(Mall_Customers)
plt.show()



print (X.shape)



from sklearn.cluster import KMeans
wcss = []



for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    


plt.plot(range(1,11), wcss, linewidth=3, color='green')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('wcss')
plt.grid()
plt.show()

kmeansmodel = KMeans(n_clusters= 5, init ='k-means++', random_state=0)
y_Predict = kmeansmodel.fit_predict(X)

#Plotting Anual Income with clor by cluster

plt.scatter(X[y_Predict == 0, 0], X[y_Predict == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_Predict == 1, 0], X[y_Predict == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_Predict == 2, 0], X[y_Predict == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_Predict == 3, 0], X[y_Predict == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_Predict == 4, 0], X[y_Predict == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.grid()
plt.show()



wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init='k-means++', random_state = 0 )
    kmeans.fit(X_1)
    wcss.append(kmeans.inertia_)
    
    
plt.plot(range(1,11),wcss, linewidth=3, color ='green')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('wcss')
plt.grid()
plt.show()

# kmeansmodel = KMeans(n_clusters= 4, init ='k-means++', random_state=0)
# y_Predict_1 = kmeansmodel.fit_predict(X_1)

# print(y_Predict_1)


# plt.scatter(X_1[y_Predict_1 == 0, 0], X_1[y_Predict_1 == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
# plt.scatter(X_1[y_Predict_1 == 1, 0], X_1[y_Predict_1 == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
# plt.scatter(X_1[y_Predict_1 == 2, 0], X_1[y_Predict_1 == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
# plt.scatter(X_1[y_Predict_1 == 3, 0], X_1[y_Predict_1 == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
# plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
# plt.title('Clusters of customers')
# plt.xlabel('Age')
# plt.ylabel('Spending Score (1-100)')
# plt.legend()
# plt.grid()
# plt.show()