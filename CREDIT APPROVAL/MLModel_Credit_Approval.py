# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:20:39 2022

@author: Jeison
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  seaborn as sns
import sqlite3

import warnings
warnings.filterwarnings('ignore')

#Connecting Data Base from SQLite

Conn = sqlite3.connect('C:\Jeison\Python\CREDIT APPROVAL\CrediApproval')


#Creating data frames 
#Is better to use data comming from sql sources and make some pre proseciong and encoding ir it is posible

Application_Record = pd.read_sql_query('SELECT * FROM application_record',Conn)
Credit_Record = pd.read_sql_query('SELECT *  FROM credit_record')







