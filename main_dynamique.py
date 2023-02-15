# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 20:57:14 2023

@author: antho
"""

from Maillage import Mesh,Triangles
from EDP import EDPsca
#from Resolution import PGD
import numpy as np
from scipy.sparse import coo_matrix
import pod
from Assemblage import *
from plot_test import *
###################################################################################
"""

"""
###################################################################################
"""
PRE-TRAITEMENT (A COMPILER UNE SEULE FOIS)
"""
# Récupération du maillage et précalcul 
Maill = Mesh("MySquare.msh")
Tri = Triangles(Maill.Noeuds,Maill.Coord,Maill.NoeudsNotBoundary)
PC = Tri.PreCalcul()
# Définition de l'équation aux dérivées partielles 
EquChaleur = EDPsca()
EquChaleur.C1(1.0)
EquChaleur.C2(1.0)
EquChaleur.Operateur("LaplacienScalaire")
# Création des matrices de masse et de rigidité
M = EquChaleur.Masse(Tri,PC)
M = M.toarray()

#M = coo_matrix(M)
K = EquChaleur.Rigidité(Tri,PC)
K = K.toarray()

#K = coo_matrix(K)
# Création de la source
EquChaleur.TypeSource = "Constante"
Amplitude = 1.0
Source = EquChaleur.Source(Amplitude)
###################################################################################
"""
PROPER ORTHOGONAL DECOMPOSITION
"""
Ne=max(Maill.Noeuds)
gho=1
cp=1
S=1
D=1
m=26
T=1
Nbr=1500
pas=T/Nbr
w=np.shape(M)
a0=0*np.ones((w[0]))
Ass1 = Assemblage(D,0,S/(gho*cp))
SM = Ass1.sec_membre(Tri,PC) 
#SM= EquChaleur.sec_membre(Tri, PC)
SM = SM.toarray()
F = np.zeros((Ne,int(T/pas)))
F=SM[0][Tri.Nn-Tri.NnWOb:Tri.Nn]
As=pod.snapshot_explicite(K, M, F, a0, m, pas)
P=pod.oper_proj(As)
(Kr,Mr,Fr)=pod.reduc(K, M, F, P)
ar0=0*np.ones((1,len(Kr)))
ar0=np.dot(P.T,a0)
Ad=pod.solve_reduc_explicite(Kr, Mr, Fr, ar0, T, pas, P)
T = np.zeros([Tri.Nn,Nbr])
for i in range(Nbr):
    T[Tri.Nn-Tri.NnWOb:Tri.Nn,i] = Ad[:,i]

pause= 0.2
result_plot(T, Maill, pause)



###################################################################################
"""
PROPER GENERALIZED DECOMPOSITION
"""
# RES = PGD(Tri,1.0,500,3,1e-3,1e-3)
# # RES.Tfin = 5e-3; RES.Ntemps = 100; RES.Mode = 5; RES.Rtol = 1e-3; RES.Stol = 1e-3
# RES.Calcul(Tri,Source,PC,K,M,EquChaleur.C1,EquChaleur.C2)
###################################################################################
"""
POST-TRAITEMENT
"""
# T = np.zeros([4,RES.Ntemps])
# for i in range(RES.Ntemps):
#     T[:,i] = RES.Rtot@RES.Stot[i,:]