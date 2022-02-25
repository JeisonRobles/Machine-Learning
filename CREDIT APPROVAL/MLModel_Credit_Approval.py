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

Conn = sqlite3.connect('C:\Jeison\Python\CREDIT APPROVAL\CreditApproval.db')


#Creating data frames 
#Is better to use data comming from sql sources and make some pre proseciong and encoding ir it is posible

Application_Record = pd.read_sql_query('SELECT * FROM application_record',Conn)
Credit_Record = pd.read_sql_query('SELECT *  FROM credit_record', Conn)

#Study Data
# print('\n\n Application Records: \n\n',
#       'Dimensions:  \n', Application_Record.shape,
#       '\n\n Null Check out for table Application Record: \n',Application_Record.isnull().sum(),
#       '\n\n Unique Values:  ', Application_Record.nunique())


# print('\n\n Credit Record: \n\n',
#       'Dimensions: \n', Credit_Record.shape,
#       '\n\nNull Check out for table Credit Record:   \n\n',Credit_Record.isnull().sum(),
#       '\n\n Unique Values: ', Credit_Record.nunique())



begin_month = pd.DataFrame(Credit_Record.groupby(['ID'])['MONTHS_BALANCE'].agg(min))
begin_month = begin_month.rename(columns={'MONTHS_BALANCE': 'begin_month'})
new_data = pd.merge(Application_Record, begin_month, how= 'left', on = 'ID')


Credit_Record['dep_value'] = None
Credit_Record['dep_value'][Credit_Record['STATUS']=='2']='Yes'
Credit_Record['dep_value'][Credit_Record['STATUS']=='3']='Yes'
Credit_Record['dep_value'][Credit_Record['STATUS']=='4']='Yes'
Credit_Record['dep_value'][Credit_Record['STATUS']=='5']='Yes'

print(Credit_Record.head(10))

