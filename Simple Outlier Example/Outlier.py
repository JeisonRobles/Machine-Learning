# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 13:03:20 2022

@author: Jeison
"""

import numpy as np
import matplotlib.pyplot as plt
from math import pi

Salario_anual_miles = np.array([16,20,15,21,19,17,33,22,31,32,56,30,22,31,30,16,2,22,23])
edades = np.array([22,22,23,23,23,23,26,27,27,28,30,30,30,30,31,32,33,34,80])
media = Salario_anual_miles.mean()
std_x = Salario_anual_miles.std()*2
media_y = edades.mean()
std_y = edades.std()*2

plt.scatter(edades,Salario_anual_miles)
plt.axhline(media_y, linestyle='--', c= 'red')
plt.axvline(media, linestyle='--', c='red')


v=media     #y-position of the center
u=media_y    #x-position of the center
b=std_x     #radius on the y-axis
a=std_y    #radius on the x-axis

t = np.linspace(0, 2*pi, 100)
plt.plot( u+a*np.cos(t) , v+b*np.sin(t) )

plt.show()