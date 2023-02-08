# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:44:01 2023

@author: arabej
"""

import numpy as np

def surface_triangle(triangle): #calcul avec la formule de Heron
    x1, y1 = triangle[0]
    x2, y2 = triangle[1]
    x3, y3 = triangle[2]
    a = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    b = np.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    c = np.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    s = (a + b + c) / 2
    return np.sqrt(s * (s - a) * (s - b) * (s - c))

def integrate_triangle(triangle, f):#la valeur de la fonction est prise au barycentre du triangle
    x1, y1 = triangle[0]
    x2, y2 = triangle[1]
    x3, y3 = triangle[2]
    x_barycenter = (x1 + x2 + x3) / 3
    y_barycenter = (y1 + y2 + y3) / 3
    area = surface_triangle(triangle)
    return area * f(x_barycenter, y_barycenter)

#test des 2 fonctions
# def f(x, y):
#     return x**2 + y**2

# triangle = [(0, 0), (1, 0), (0, 1)]
# surface = surface_triangle(triangle)
# print("Surface du triangle=:", surface)

# integral = integrate_triangle(triangle, f)
# print("L'integrale de la fonction sur le triangle=:", integral)



