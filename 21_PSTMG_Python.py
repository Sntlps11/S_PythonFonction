# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:02:30 2020

@author: Ludovic FONQUERGNE
"""
#
#
##### Algorithme #####
init=int(input("Rang initial = "))
u=float(input("Terme initial = "))
n=int(input("Rang à calculer = "))
while init<n:
    u=2*u+2
    init=init+1
print("u",init,"=",u)
#
#
##### Instructions conditionnelles #####
#
#
##### 1 condition if
a,b = 8,0
if b!=0:
    div=a/b
    print(div)
#
#
##### 2 conditions if ... else
x=-1
if x<=2:
    y=x**2
else:
    y=2*x+1
print (y)
#
#
##### 3 conditions if ... elif ... else
x=3
if x<0:
    print("négatif")
elif x==0:
    print("nul")
else:
    print("positif")
#
#
##### Boucles bornées ou non #####
#
#
##### Boucle bornée
for i in range(5):
    print(i**2)
#
#
##### Boucle non bornée
i=0
while i<5:
    print(i**2)
    i=i+1
#
#
##### Somme des n premiers impairs
n=int(input("Nb d'impairs ="))
s=0
for i in range(1,2*n,2):
    s=s+i
print(s)
#
#
##### Sommes des impairs jusqu’à un total minimal de 50
s=0
i=1
while s<50:
    s=s+i
    i=i+2
print(s)
#
#
##### Bibliothèques ou modules #####
#
#
##### Constitution d’une bibliothèque
from Surfaces import*

l=float(input("longueur ="))
b=float(input("base ="))
h=float(input("hauteur = "))

print(Srectangle(l,h))
print(Striangle(b,h))
print(Scarre(l))
print(Sdisque(b))
print(Scarre(5))
#
#
##### Simulations du hasard #####
#
#
##### Affichage de tous les résultats
from random import*

n=int(input("Nb de lancers = "))
for i in range(1,n+1):
    print("Lancer ",i," =",randint(1,6))
#
#
##### Affichage de tous les résultats
from random import*

def lance_de(n):
    L=[randint(1,6) for i in range(n)]
    return L
lance_de(15)
#
#
##### Représentations graphiques #####
#
#
##### par défaut
import matplotlib.pyplot as plt

abscis=[-2+i*.04 for i in range(101)]
ordon=[x**2 for x in abscis]
plt.plot(abscis,ordon)
plt.show()
#
#
##### pointillés rouge et grille
import matplotlib.pyplot as plt

abscis=[-2+i*.04 for i in range(101)]
ordon=[x**2 for x in abscis]
plt.plot(abscis,ordon,'r--')
plt.grid()
plt.show()
#
#
##### Listes #####
#
#
##### par extension
L=list(range(1,15,2))
print(L)
#
#
##### par ajouts successifs
J=["lundi","mardi","mercredi","jeudi","vendredi","samedi"]
J.append("dimanche")
print(J)
#
#
##### par compréhension
L=[x**2 for x in range(4)]
print(L)

I=[1,3,5,7,9]
Carre=[x**2 for x in I if x<7]
print(Carre)
#
#
##### Opérations sur les listes
lp=[1,3,5,3]
lp.insert(2,4)
print(lp)
lp.insert(3,1)
print(lp)
lp.remove(1)
print(lp)
del lp[4]
print(lp)
print(lp[1],lp[-1],lp[2],lp[-2])
result=[2*x-3 for x in lp]
print(result)
#
#
##### Multiples de 13 inférieurs à 100
L=[0]*8
for i in range(8):
    L[i]=13*i
print(L)

L=[]
for i in range(8):
    L.append(13*i)
print(L)

L=[]
for n in range(0,100,13):
    L.append(n)
print(L)

L=[]
i=0
while 13*i<=100:
    L.append(13*i)
    i=i+1
print(L)

L=[]
n=0
while n<=100:
    L.append(n)
    n=n+13
print(L)

L=[13*i for i in range(8)]
print(L)

L=[n for n in range(0,101,13)]
print(L)

L=[n for n in range(101) if n%13==0]
print(L)