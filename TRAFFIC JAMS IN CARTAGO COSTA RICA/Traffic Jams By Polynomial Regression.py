#!/usr/bin/env python
# coding: utf-8

# # Traffic Jams in Cartago City, Costa Rica

# ## By Jeison Robles Arias

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[25]:


Jam = pd.read_excel(r'C:\Jeison\Python\Traffic Jams\Cartago Jams.xlsx')


# In[26]:


Jam.head()


# # Making some Math

# #### Calculamos la duracion promedio

# In[27]:


Jam['Duracion Promedio'] = (Jam['Duracion Minima'] + Jam['Duracion Maxima']) / 2
Jam.head()


# In[28]:


Jam['Duracion Minima Por Km (min/Km)'] = Jam['Duracion Minima'] / Jam['Distancia (km)']
Jam['Duracion Maxima Por Km (min/Km)'] = Jam['Duracion Maxima'] / Jam['Distancia (km)']
Jam['Duracion Promedio Por Km (min/Km)'] = Jam['Duracion Promedio'] / Jam['Distancia (km)']
Jam.head()


# # Exploratory Stage

# In[ ]:





# In[40]:


plt.rcParams['figure.figsize'] = (15,10)
plt.scatter(Jam['Hora Entera'], Jam['Duracion Promedio Por Km (min/Km)'], s= 100)
plt.scatter(Jam['Hora Entera'], Jam['Duracion Minima Por Km (min/Km)'], s= 10, c = 'green')
plt.scatter(Jam['Hora Entera'], Jam['Duracion Maxima Por Km (min/Km)'], s= 10, c = 'red')
plt.title('Duracion Promedio min/Km Vs Hour of day')
plt.xlabel('Hour')
plt.ylabel('Duracion min/Km')
plt.grid()


# We can detect by simply observing that there are somo typical values as TOPs focus on 7 am and 5pm

# The trends still no mather if is average, Max or Min

# _ H Refiere a Holydays for increasing traffic Jams

# In[76]:


X = Jam.iloc[:,11].values
y = Jam.iloc[:,15].values
X.shape

X_H = Jam.iloc[:,11].values
y_H = Jam.iloc[:,14].values


# In[77]:


from sklearn.linear_model import LinearRegression

LR = LinearRegression()
LR.fit(X.reshape(-1,1), y)

LR_H = LinearRegression()
LR.fit(X.reshape(-1,1), y)


# In[52]:


from sklearn.preprocessing import PolynomialFeatures


# In[78]:


poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X.reshape(-1,1))
poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)



poly_reg_H = PolynomialFeatures(degree = 4)
X_poly_H = poly_reg_H.fit_transform(X_H.reshape(-1,1))
poly_reg.fit(X_poly_H, y)
lin_reg_2_H = LinearRegression()
lin_reg_2_H.fit(X_poly_H, y)


# In[57]:


plt.rcParams['figure.figsize'] = (15,10)
plt.scatter(Jam['Hora Entera'], Jam['Duracion Promedio Por Km (min/Km)'], s= 100)
plt.plot(X.reshape(-1,1), LR.predict(X.reshape(-1,1)), color = 'blue')
plt.title('Duracion Promedio min/Km Vs Hour of day')
plt.xlabel('Hour')
plt.ylabel('Duracion min/Km')
plt.grid()


# In[80]:


X = X.reshape(-1,1)
plt.scatter(X, y, color = 'red')
plt.scatter(Jam['Hora Entera'], Jam['Duracion Promedio Por Km (min/Km)'], s= 100)
plt.scatter(Jam['Hora Entera'], Jam['Duracion Minima Por Km (min/Km)'], s= 10, c = 'green')
plt.scatter(Jam['Hora Entera'], Jam['Duracion Maxima Por Km (min/Km)'], s= 10, c = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.plot(X, lin_reg_2_H.predict(poly_reg_H.fit_transform(X)), color = 'purple')
plt.title('Duracion Promedio min/Km Vs Hour of day')
plt.grid()
plt.xlabel('Hour')
plt.ylabel('Duracion min/Km')


# In[70]:


lin_reg_2.predict(poly_reg.fit_transform([[23]]))


# In[ ]:




