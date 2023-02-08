# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:51:07 2023

@author: mehdi
"""

import numpy as np
import scipy as sp
import pod

# Ne=int(input("le nombre de noeud:"))
# m=int(input("nombre de mode/snapshots: "))
# T=int(input("temps final :"))
Ne=10
m=3
T=10
pas=1
M=np.ones((Ne,Ne))
N=np.eye(Ne)
F=np.ones((Ne,int(T/pas)))
a0=20*np.ones((1,Ne))

# début de la résolution

As=pod.snapshot(M, N, F, a0, m, pas)
P=pod.oper_proj(As)
(Mr,Nr,Fr)=pod.reduc(M, N, F, P)
ar0=20*np.ones((1,len(Mr)))
Ad=pod.solve_reduc(Mr, Nr, Fr, ar0, T, pas, P)


