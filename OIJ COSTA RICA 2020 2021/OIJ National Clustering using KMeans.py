#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[89]:


oij = pd.read_csv("C:\Jeison\Python\OIJ Analysis\Estadisticas.csv")


# In[90]:


oij.shape


# In[91]:


oij = oij.drop(['Rango Horarios', 'Nacionalidad', 'Victima','Delito','Genero','Fecha'], axis = 1)


# In[93]:


oij.head()


# In[94]:


from sklearn import preprocessing


# In[95]:


le = preprocessing.LabelEncoder()


# In[96]:


Cluster = oij


# In[97]:


Cluster['SubDelito'] = le.fit_transform(Cluster['SubDelito'])
Cluster['SubVictima'] = le.fit_transform(Cluster['SubVictima'])
Cluster['Edad'] = le.fit_transform(Cluster['Edad'])
Cluster['Provincia'] = le.fit_transform(Cluster['Provincia'])
Cluster['Canton'] = le.fit_transform(Cluster['Canton'])


# In[98]:


Cluster.max()


# ## NORMALIZACION

# In[99]:


from sklearn.preprocessing import StandardScaler


# In[100]:


ss = StandardScaler()


# In[101]:


Cluster[['SubDelito','SubVictima','Edad','Provincia','Canton','Hora Inicial','Mes']] = ss.fit_transform(Cluster[['SubDelito','SubVictima','Edad','Provincia','Canton','Hora Inicial','Mes']])


# In[102]:


Cluster.head()


# ## PLOTTING

# In[103]:


sns.pairplot(Cluster)


# In[104]:


plt.rcParams['figure.figsize'] = (20,20)
sns.heatmap(Cluster.corr(), cmap= 'Wistia', annot = True)
plt.title('Heatmap')
plt.show()


# In[105]:


Cluster.head()


# # CLUSTERING CANTONES VS SUB VICTIMAS

# In[107]:


plt.scatter(Cluster.iloc[:,[5]],Cluster.iloc[:,[2]])
plt.title('Exploratory Cantones vs Sub Victimas')
plt.xlabel('Cantones')
plt.ylabel('Sub Victimas')
plt.grid()
plt.show()


# ### Finding K numbers by Elbow Method

# In[117]:


from sklearn.cluster import KMeans


# In[118]:


x = Cluster.iloc[:,[5, 2]].values


# In[119]:


x.shape


# In[120]:


wcss = []

for i in range(1,20):
    km = KMeans(n_clusters=i, init = 'k-means++',max_iter=300, n_init=10, random_state=0)
    km.fit(x)
    wcss.append(km.inertia_)


# In[121]:


plt.plot(range(1,20), wcss)
plt.title('Elbow')
plt.xlabel('No of clusters')
plt.ylabel('wcss')
plt.grid()
plt.show()


# In[122]:


km = KMeans(n_clusters=9, init = 'k-means++',max_iter=300, n_init=10, random_state=0)
y_mean = km.fit_predict(x)


# In[130]:


plt.scatter(x[y_mean == 0,0], x[y_mean == 0,1], s= 50, color = 'pink' )
plt.scatter(x[y_mean == 1,0], x[y_mean == 1,1], s= 50, color = 'blue')
plt.scatter(x[y_mean == 2,0], x[y_mean == 2,1], s= 50, color = 'green')
plt.scatter(x[y_mean == 3,0], x[y_mean == 3,1], s= 50, color = 'purple')
plt.scatter(x[y_mean == 4,0], x[y_mean == 4,1], s= 50, color = 'orange')
plt.scatter(x[y_mean == 5,0], x[y_mean == 5,1], s= 50, color = 'brown')
plt.scatter(x[y_mean == 6,0], x[y_mean == 6,1], s= 50, color = 'cyan')
plt.scatter(x[y_mean == 7,0], x[y_mean == 7,1], s= 50, color = 'magenta')
plt.scatter(x[y_mean == 8,0], x[y_mean == 8,1], s= 50, color = 'black')

plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1], s= 300, color = 'red')

plt.style.use('fivethirtyeight')
plt.title('Clustering with 9 K')
plt.xlabel('Canton')
plt.ylabel('Sub Victima')
plt.show()

