# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:11:52 2023

@author: mehdi
"""

import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from Maillage import *

def result_plot(Ad,Maill,t):
    L=[]
    x=[0 for i in range (max(Maill.Noeuds))]
    y=[0 for i in range (max(Maill.Noeuds))]
    for i in range (len(Maill.Noeuds)):           
        if Maill.Noeuds[i] not in L:
            x[int(Maill.Noeuds[i]-1)]=Maill.Coord[int(3*i)]
            y[int(Maill.Noeuds[i]-1)]=Maill.Coord[int(3*i+1)]
            L=L+[Maill.Noeuds[i]]

    triang = mtri.Triangulation(x, y)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    ax.triplot(triang, c="#D3D3D3", marker='.', markerfacecolor="#DC143C",
               markeredgecolor="black", markersize=10)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.show()
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    
    ax.plot_trisurf(triang, Ad.T[t], cmap='jet')
    ax.scatter(x,y,Ad.T[t], marker='.', s=10, c="black", alpha=0.5)
    ax.view_init(elev=60, azim=-45)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('T')
    plt.show()