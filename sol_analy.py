# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:05:03 2023

@author: arabej

Resolution analytique de ∂T/∂t - D∇^2T = S / (ρ * Cp),Dans ce cas, les conditions initiales sont
 T(x,y,0) = T_init et les conditions aux limites sont de type Dirichlet, ce qui signifie que
 la température T est fixée à une valeur T_bord sur le bord du carré,
 La solution générale de l'équation de la chaleur avec des conditions initiales et aux limites de ce
 type peut être exprimée en utilisant la méthode de séparation des variables, en supposant que 
 la solution peut être écrite comme une somme de fonctions de la forme T(x,y,t) = X(x)Y(y)Z(t).
 T(x,y,t) = T_0 + S/(4πk) * exp(-λt) * 
 ∑[n=1 à l'infini] [∑[m=1 à l'infini] A_nm * sin(nπx/L) * sin(mπy/L)] * exp(-λn^2 + m^2)t.
où T_0 est la température moyenne dans le domaine, L est la longueur du domaine carré, et 
λ est donné par λ = (n^2 + m^2)π^2/(4L^2). Les coefficients A_nm sont donnés par :
A_nm = (8/k) * S * ρ * Cp * [(-1)^(n+m) / (nmπ)] * [1 - exp(-Dλn^2t/L^2)] * [1 - exp(-Dλm^2t/L^2)] * 
∫[0 à L] ∫[0 à L] T_init * sin(nπx/L) * sin(mπy/L) dx dy
où l'intégrale est prise sur tout le domaine carré.(k=D*rho*Cp) c'est la conductivité"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Définition des paramètres
D = 0.022   # coefficient de diffusion
rho = 1.3  # densité
Cp = 1007   # capacité thermique
S = 1.0   # source de chaleur
T_init = 25   # condition initiale
T_bord = 25   # condition aux limites de type Dirichlet sur les bords
L = 1.0   # longueur du domaine carré
n_max = 20   # nombre de termes dans la série de Fourier
eps = 1e-10  # tolérance pour éviter les divisions par zéro

# Calcul de la solution analytique
def analytic_T(x, y, t):
    T0 = np.mean(T_bord)   # température moyenne
    T = T0 + S / (4 * np.pi * D*rho*Cp) * np.exp(-n_max**2 * np.pi**2 * t / (4 * L**2)) * \
        np.sum([np.sum([(8 / (D * rho * Cp * n * m * np.pi)) * \
                        ((-1)**(n + m) / (1 - (n**2 / (n_max**2 + eps))) / (1 - (m**2 / (n_max**2 + eps)))) * \
                        (1 - np.exp(-D * (n**2 + m**2) * np.pi**2 * t / L**2)) * \
                        np.sin(n * np.pi * x / L) * np.sin(m * np.pi * y / L) for n in range(1, n_max + 1)]) \
                for m in range(1, n_max + 1)])
    return T


# Coordonnées des points à tracer
points = [(0.1, 0.1), (0.3, 0.3), (0.5, 0.5), (0.7, 0.7), (0.9,0.9)]
n = 100 #le nombre de pas de temps
dt=0.0001  #le pas de temps 
# Tracer la température en fonction du temps pour chaque point
fig, ax = plt.subplots()
for x_point, y_point in points:
    T_point = [analytic_T(x_point, y_point, t) for t in np.arange(n) * dt]
    ax.plot(np.arange(n) * dt, T_point, label=f'({x_point}, {y_point})')
ax.set_xlabel('Temps')
ax.set_ylabel('Température(C)')
ax.legend()
plt.show()

