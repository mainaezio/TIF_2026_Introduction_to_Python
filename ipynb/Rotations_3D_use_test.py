# Questo programma mostra come utilizzare un modulo scritto
# dall'utente in un programma in Python


import numpy as np
import Rotations_3D_numpy

vv = np.matrix([[1],[2],[3]])
ang = np.pi/4

res = Rotations_3D_numpy.Rx(ang,vv)
print(res)