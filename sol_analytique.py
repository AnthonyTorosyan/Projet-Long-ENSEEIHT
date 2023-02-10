# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:53:08 2023

@author: arabej 
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Nous allons définir les conditions aux limites pour x et y
x_min, x_max = 0, 1
y_min, y_max = 0, 1
# Nous allons définir le nombre de points de grille dans x et y
nx, ny = 51, 51
# Nous allons définir les constantes pour l'air
D = 0.022 #  (D en w/m/K)
S = 1
rho = 1.3
Cp = 1007
# Nous allons définir le pas d'espace et de temps
dx = (x_max - x_min) / (nx - 1)
dy = (y_max - y_min) / (ny - 1)
dt = 0.001
# Nous allons définir le vecteur de la grille x et y
x = np.linspace(x_min, x_max, nx)
y = np.linspace(y_min, y_max, ny)


# Nous allons définir la matrice de la température T avec des conditions initiales nulle
T = np.zeros((nx, ny))
# Boucle principale pour la mise à jour de la température
nt = 1000 # Nombre de pas de temps
T_evolution = np.zeros((nt, nx, ny)) # Enregistrement de la température à chaque instant
for n in range(nt):
    Tn = T.copy()
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            T[i, j] = Tn[i, j] + D * dt / dx**2 * (Tn[i+1, j] - 2 * Tn[i, j] + Tn[i-1, j]) + \
                      D * dt / dy**2 * (Tn[i, j+1] - 2 * Tn[i, j] + Tn[i, j-1]) + \
                      S / (rho * Cp) * dt
    T_evolution[n, :, :] = T # Enregistrement de la température à l'instant n


# Visualisation de la température en fonction du temps pour plusieurs points
i_points = [0, 10,25,35, nx-1]
j_points = [0, 10,25,35, ny-1]
# Boucle pour visualiser la température en fonction du temps pour chaque point sélectionné
for i, j in zip(i_points, j_points):
    plt.plot(range(nt), T_evolution[:, i, j], label='Point ({}, {})'.format(i, j))

plt.xlabel('Temps (nt)')
plt.ylabel('Température (T)')
plt.legend()
plt.show()

#le graphe animé de la temperature sur la grille en fonction du temps
#(!!à compiler sur vs_code ps compatible avec spyder) 
# Initialisation de la figure
fig = plt.figure()
ax = plt.axes()
im = ax.imshow(T, origin='lower', extent=[x_min, x_max, y_min, y_max], cmap='hot')
plt.colorbar(im)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Evolution de la temperature')
# La fonction d'animation
def animate(i):
    im.set_data(T_evolution[i, :, :])
    return im,
ani = animation.FuncAnimation(fig, animate, frames=nt, interval=50, blit=True)
plt.show()




