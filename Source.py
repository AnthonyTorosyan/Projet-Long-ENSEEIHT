# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:41:58 2023

@author: zekri
"""
import numpy as np

class Source:
    def __init__(self,typesource):
        """
        Construction d'une source. Elle permet de créer un tenseur contenant 
        la valeur de la source pour tout les noeuds du maillage pour chaque pas de temps
        Choix de source:
            - source constante: une source fixe dans le temps
            - source "diffusion 1" : s = 1 + 2 x t
            -source "diffusion 2" : s=B(u) avec u est une solution qui
                admet une représentation séparée d'ordre 5 (voir le papier nouy_2010.pdf page 1616)
        """
        self.TypeSource = typesource
    def getSource(self):
        return self.TypeSource
    def Source(self,source):
        self.TypeSource = source
        
class constante(Source):
    def __init__(self,Amp,Npas):
        Amplitude=np.zeros((len(Amp),Npas))
        for i in range (Npas):
            Amplitude.T[i]=Amp                   
        self.val=Amplitude
    def getval(self):
        return self.val        
class diffusion1(Source):
    def __init__(self,Maill,Tf,Npas):
        L=[]
        n=max(Maill.Noeuds)
        s=np.zeros((n,Npas))
        x=[0 for i in range (n)]
        for i in range (len(Maill.Noeuds)):           
            if Maill.Noeuds[i] not in L:
                x[int(Maill.Noeuds[i]-1)]=Maill.Coord[int(3*i)]
                L=L+[Maill.Noeuds[i]]
        for j in range(Npas):
            for i in range(n):
                s[i,j] = 1 + 2*x[i]*j*Tf/Npas
        self.val=s
    def getval(self):
        return self.val                
class diffusion2(Source):
    def __init__(self,Maill,Tf,Npas):
        n=max(Maill.Noeuds)
        s=np.zeros((n,Npas))
        for j in range(Npas):
            t=j*Tf/Npas
            L=[]
            for i in range (len(Maill.Noeuds)):
                if Maill.Noeuds[i] not in L:
                    x=Maill.Coord[int(3*i)]
                    y=Maill.Coord[int(3*i+1)]
                    ut=np.sin(np.pi*x)*np.sin(np.pi*y)-1/2*np.sin(np.pi*x)*np.sin(2*np.pi*y)+np.pi/2*np.sin(2*np.pi*x)*np.sin(np.pi*y)*np.cos(np.pi*t)+2*np.pi/3*np.sin(2*np.pi*x)*np.sin(2*np.pi*y)*np.cos(2*np.pi*t)+4*np.pi/5*np.sin(4*np.pi*x)*np.sin(4*np.pi*y)*np.cos(4*np.pi*t)
                    us=-2*np.pi**2*np.sin(np.pi*x)*np.sin(np.pi*y)*t-5/4*np.pi**2*np.sin(np.pi*x)*np.sin(2*np.pi*y)*(1-t)-3/4*np.pi**2*np.sin(2*np.pi*x)*np.sin(np.pi*y)*np.sin(np.pi*t)-8/3*np.pi**2*np.sin(2*np.pi*x)*np.sin(2*np.pi*y)*np.sin(2*np.pi*t)-32/5*np.pi**2*np.sin(4*np.pi*x)*np.sin(4*np.pi*y)*np.sin(4*np.pi*t)
                    s[int(Maill.Noeuds[i]-1),j]=ut-us
                    L=L+[Maill.Noeuds[i]]
        self.val=s
    def solution_analytique(self,Maill,Tf,Npas):
        n=max(Maill.Noeuds)
        s_analy=np.zeros((n,Npas))
        for j in range(Npas):
            t=j*Tf/Npas
            L=[]
            for i in range(len(Maill.Noeuds)):
                if Maill.Noeuds[i] not in L:
                    x=Maill.Coord[int(3*i)]
                    y=Maill.Coord[int(3*i+1)]
                    s_analy[int(Maill.Noeuds[i]-1),j]= np.sin(np.pi*x)*np.sin(np.pi*y)*t +1/2 * np.sin(np.pi*x)*np.sin(2*np.pi*y)*(1-t) +1/2 * np.sin(2*np.pi*x)*np.sin(np.pi*y)*np.sin(np.pi*t)+ 1/3 * np.sin(2*np.pi*x)*np.sin(2*np.pi*y)*np.sin(2*np.pi*t)+ 1/5* np.sin(4*np.pi*x)*np.sin(4*np.pi*y)*np.sin(4*np.pi*t)
                    L=L+[Maill.Noeuds[i]]
        return s_analy
    
            
                    
                                
        
        