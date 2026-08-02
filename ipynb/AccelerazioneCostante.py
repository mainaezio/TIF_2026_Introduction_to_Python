#!/usr/bin/env python
# coding: utf-8

# ##  MOTO CON ACCELARAZIONE COSTANTE CON numpy
# ##  Asse y diretto verso l'alto

import numpy as np

gconst = -9.81 # m/s**2

def posy_t(y0,v0,t):
    return 0.5*gconst*t**2 + v0*t + y0

def vely_t(v0,t):
    return gconst*t + v0

def abs_vely_y(y0,v0,y):
    v_sq = 2.*gconst*(y-y0) + v0**2
    return np.sqrt(v_sq)

def pos(x0,y0,v0x,v0y,t):
    x = v0x*t
    y = posy_t(y0,v0y,t)
    return x, y

def vel(v0x,v0y,t):
    return v0x, vely_t(v0y,t)


def time_y(y0,v0,y):
    """
    tempo in cui la particella e' ad altezza y
    """
    cutoff = 1.e-12
    a = 0.5*gconst
    b = v0
    c = y0-y
    discr = (b**2-4.*a*c)
    if(abs(discr) < cutoff):
        t1 = -0.5*b/a
        t2 = None
    elif discr > cutoff:
        delta = np.sqrt(discr)
        t1 = -0.5*(b+delta)/a
        t2 = -0.5*(b-delta)/a
    else:
        t1 = None
        t2 = None

    return t1,t2


def time_v(v0,v):
    return (v-v0)/gconst