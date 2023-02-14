# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:50:48 2023

@author: arabej
"""

from Maillage import Mesh,Triangles
from EDP import EDPsca
from Resolution import PGD
import numpy as np



M_without_boundary = np.delete(np.delete(M, boundary_indices, axis=0), boundary_indices, axis=1)
K_without_boundary = np.delete(np.delete(K, boundary_indices, axis=0), boundary_indices, axis=1)
