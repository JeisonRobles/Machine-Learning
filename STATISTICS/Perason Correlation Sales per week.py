#!/usr/bin/env python
# coding: utf-8

# # PEARSON CORRELATION

# #### Jeison Robles Arias

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[36]:


#lets use the next:
#HPW = HOURS PER WEEK
#SPE = SALES PER WEEK

HPW = [40,56,50,82,41,51,45,90,47,72]
SPW = [179480.58, 2495037.73, 2285369.51, 2367896.33, 1309745.16, 623013.69, 2989943.37, 1970316.34, 1845840.39, 2553231.33]


# In[37]:


len(HPW)


# In[38]:


len(SPW)


# #### *Initial Plotting*

# In[39]:


plt.scatter(HPW, SPW, s = 100 , c= 'purple')
plt.title('HPW vs SPW')
plt.xlabel('HPW')
plt.ylabel('SPW')
plt.grid()


# Means 

# In[40]:


Mean_HPW = np.mean(HPW)
Mean_SPW = np.mean(SPW)


# In[41]:


Mean_HPW


# In[42]:


Mean_SPW


# Pearson Correlation (r)

# Numerator Function

# In[43]:


def numerator(HPW, SPW, Mean_HPW, Mean_SPW):
    Sum_Num = 0
    for i in range(len(HPW)):
        Sum_Num = Sum_Num + (HPW[i-1] - Mean_HPW) * (SPW[i-1] -Mean_SPW)
    return Sum_Num


# In[44]:


print(numerator(HPW, SPW, Mean_HPW, Mean_SPW))


# Denominator Function

# In[57]:


def denominator(HPW, SPW, Mean_HPW, Mean_SPW):
    Sum_Den1 = 0
    Sum_Den2 = 0
    Sum_Den = 0
    
    for i in range(len(HPW)):
        Sum_Den1 = Sum_Den1 + np.power((HPW[i-1] - Mean_HPW),2) 
    
    Sum_Den1 = np.sqrt(Sum_Den1)
   
    for i in range(len(SPW)):
        Sum_Den2 = Sum_Den2 + np.power((SPW[i-1] - Mean_SPW),2)
    
    Sum_Den2 = np.sqrt(Sum_Den2)

    Sum_Den = Sum_Den1 * Sum_Den2
    
    return Sum_Den


# r Correlation

# In[58]:


r = numerator(HPW, SPW, Mean_HPW, Mean_SPW) / denominator(HPW, SPW, Mean_HPW, Mean_SPW)


# In[59]:


print('The Pearson Correlation r is iqual to: \t', r)


# *Acording to the book SQL for data Analysis this correlations is between 0.2 ans 0.4 absolute value, This 'r' correlation is MODERATE POSITIVE CORRELATION*
