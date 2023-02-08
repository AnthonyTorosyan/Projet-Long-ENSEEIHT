# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 10:02:48 2023

@author: ZEKRI
"""


import numpy as np
import scipy as sp

def snapshot(M,N,F,a0,m,pas):   #M et N et F les matrices et le second membre du système d'équation différentiel couplé
                              # a0 le point de départ C.I
                          # n le nombre d'itérations
    As=np.zeros((len(M),m))
    As.T[0]=a0
    #P, L, U=sp.linalg.lu(N)
    Ninv=np.linalg.inv(N)      
    for i in range (m-1):
        #sec_membre=F[:][i]-M*As[:][i]
        #dAdt=np.linalg.solve(N,sec_membre)
        As.T[i+1]=As.T[i]+pas*np.dot(Ninv,F.T[i]-np.dot(M,As.T[i]))
    return As
        

def oper_proj(As):
    u,s,v=np.linalg.svd(As)
    sigma=np.zeros((len(As),len(s)))
    for i in range (len(s)):
        sigma[i][i]=s[i]
    P=np.dot(u,sigma)
    return P

def reduc(M,N,F,P):
    Mr=np.dot(np.transpose(P),np.dot(M,P))
    Nr=np.dot(np.transpose(P),np.dot(N,P))
    Fr=np.dot(np.transpose(P),F)
    return (Mr,Nr,Fr)

def solve_reduc(Mr,Nr,Fr,ar0,T,pas,P):
    Ar=np.zeros((len(Mr),int(T/pas)))
    Ar.T[0]=ar0
    #P, L, U=sp.linalg.lu(N)
    Ninv=np.linalg.inv(Nr)      
    for i in range (int(T/pas)-1):
        #sec_membre=F[:][i]-M*As[:][i]
        #dAdt=np.linalg.solve(N,sec_membre)
        Ar.T[i+1]=Ar.T[i]+pas*np.dot(Ninv,Fr.T[i]-np.dot(Mr,Ar.T[i]))
    Ad=np.dot(P,Ar)    
    return Ad
    
    
    
        
