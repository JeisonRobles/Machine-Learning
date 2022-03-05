#!/usr/bin/env python
# coding: utf-8

# # Calculating Statistics measurements

# ### Jeison Robles Arias

# In[39]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[40]:


x = [1,2,3,4,5,6,7,8,9,10,11]
y = [5000,1700,8200,1500,3300,9000,2000,0,0,2300,4700]


# In[41]:


plt.scatter(x,y, s = 100, c= 'purple')
plt.title('Add on Sales')
plt.xlabel('unit')
plt.ylabel('Price')
plt.grid()


# Calculating range

# In[42]:


Max_y = np.max(y)
Min_y = np.min(y)
Range = Max_y - Min_y
print(Range)


# Calculating the mean

# In[43]:


Mean_y = np.mean(y)
print(Mean_y)


# Calculating Sample Standard Deviation

# In[44]:




def std (y):
    Sum_Dif = 0
    for i in range(11):
        Sum_Dif = Sum_Dif +  np.power((y[i] - Mean_y),2)
    
    S_Std = np.sqrt(Sum_Dif/ (len(y)-1))
    return S_Std


# In[45]:


std(y)


# Calculating Quartiles, first brake points

# In[46]:


# Going to use k = 4
n = 4

#Calculating Brake points

k = 1
i1 = ((k/n)*(len(y)-1))+1
k = 2
i2 = ((k/n)*(len(y)-1))+1
k = 3
i3 = ((k/n)*(len(y)-1))+1

print('i1= ',i1, '\ni2= ', i2,'\ni3 = ', i3)


# Sorting to determine Quartiles

# In[48]:


print(y)
y.sort()
print(y)


# In[55]:


Q1 = y[int(i1-1)] + (y[int(i1+1-1)] - y[int(i1-1)])/2
Q1



# In[60]:


Q3 = y[int(i3-1)] + (y[int(i3+1-1)] -y[int(i3-1)])/2
Q3


# In[62]:


IQR = Q3 - Q1
IQR


# ### Outliers

# In[64]:


Minimum_Aceptable_Value = Q1 - 1.5*IQR
Maximum_Aceptable_Value = Q3 + 1.5*IQR
print('Min_Tol_Val= ', Minimum_Aceptable_Value, '\n','Max_Tol_Val=' , Maximum_Aceptable_Value)


# ## *There is no Outliers detected*
