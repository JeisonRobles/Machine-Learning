# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 07:11:57 2022

@author: Jeison
"""


import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve
from sklearn.metrics import average_precision_score

































x = np.array([12,13,14,19,21,23])
y = np.array ([12,13,14,19,21,23,450])

def grubbs_test(x):
    n = len(x)
    mean_x = np.mean(x)
    sd_x = np.std(x)
    numerator = max(abs(x - mean_x))
    g_calculated = numerator/sd_x
    print('Grubb Calculated is:', g_calculated)
    t_value = stats.t.ppf(1 - 0.05 / (2 * n), n - 2)
    g_critical = ((n - 1) * np.sqrt(np.square(t_value))) / (np.sqrt(n) * np.sqrt(n - 2 + np.square(t_value)))
    print('El valor critico de Grubb es: ',g_critical)
    
    if g_critical >g_calculated:
        print('From grubbs test we observe that calculated value is lesser than critical value, Accept null hypoyhesis and conclude that there is no outliers\n')
        
    else:
        print('From grubbs test we observe that calculated value is greater than critical value, Reject null Hypothesis and conclude that there is an outlier\n')
        
    
    

grubbs_test(x)
grubbs_test(y)