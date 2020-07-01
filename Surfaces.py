# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:27:47 2020

@author: Ludovic FONQUERGNE
"""
from math import*

def Scarre(c):
    return c**2

def Sdisque(r):
    return pi*r**2

def Srectangle(l,h):
    return l*h

def Striangle(b,h):
    return b*h/2

def Strapeze(b,B,h):
    return (b+B)*h/2