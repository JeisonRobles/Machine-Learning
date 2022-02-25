# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 23:00:04 2022

@author: Jeison
"""

import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

conn = sqlite3.connect(r"C:\Jeison\Python\OIJ Analysis\OIJ.db")

cur = conn.cursor()

# cur.execute('SELECT * FROM Estadisticas')

OIJ_DF = pd.read_sql_query('SELECT * FROM Estadisticas', conn)
OIJ_DF =OIJ_DF.iloc[:,[0,1,2,3,4,5,6,7,8,9,10]]
# print(OIJ_DF.head(10))
print(OIJ_DF.shape)

#Plot first keys

# OIJ_DF['Delito'].value_counts().head(100).plot(kind= 'barh')
# OIJ_DF['SubDelito'].value_counts().head(10).plot(kind='barh')

# #Lets focus on most important Crime that's Hurto

OIJ_DF_Hurto = OIJ_DF[OIJ_DF.Delito == 'Hurto']
print(OIJ_DF_Hurto.shape)