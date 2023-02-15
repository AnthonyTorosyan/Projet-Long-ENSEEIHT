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
import matplotlib.animation as animation


def result_plot(Ad, Maill, pause):
    L=[]
    x=[0 for i in range (max(Maill.Noeuds))]
    y=[0 for i in range (max(Maill.Noeuds))]
    for i in range (len(Maill.Noeuds)):           
        if Maill.Noeuds[i] not in L:
            x[int(Maill.Noeuds[i]-1)]=Maill.Coord[int(3*i)]
            y[int(Maill.Noeuds[i]-1)]=Maill.Coord[int(3*i+1)]
            L=L+[Maill.Noeuds[i]]

    triang = mtri.Triangulation(x, y)
    #---------------------------------- visualisation du mesh---------------------------------------
    # fig = plt.figure()
    # ax = fig.add_subplot(1,1,1)
    # ax.triplot(triang, c="#D3D3D3", marker='.', markerfacecolor="#DC143C",
    #             markeredgecolor="black", markersize=10)
    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    # plt.show()
    #---------------------------------------------------------------------------------
    sh=np.shape(Ad)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    for i in range(sh[1]):
        t = i 
        ax.plot_trisurf(triang, Ad.T[int(t)], cmap='jet')
        # ax.view_init(elev=60, azim=-45)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('T')
        plt.pause(pause) 


    plt.show()
    
