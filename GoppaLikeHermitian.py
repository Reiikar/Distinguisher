# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:52:45 2023

@author: jade

étude Goppa-like Hermitien
"""

import scipy.special
import math

q=11;
m=2;
assert  m%2 == 0;
q0=q**(m//2);
g=q0*(q0-1)//2;
#On va se permettre de faire varier la longueur entre e*q0^3 et q0^3 pour 0<e<=1 
 #Fraction du nombre de points rationels total qu'on évalue
e_min=1;
e_max=1
nbpts=q0**3;
n=nbpts

min_t=64; #Le minimum d'erreurs qu'on veut décoder
min_WK=128; #La sécurité minimum acceptée
max_KS= 2*10**7#Taille de clé maximum

min_s= 2*min_t+2*g-2;
max_s=nbpts;

def Study(n,s):
    k=n-m*(s-g+1);
    if k <=0 :
        return None;
    t=s//2-g+1;
    if t < min_t :
        return None;
    KeySize= math.floor(math.log2(q)*k*(n-k)/8)
    if KeySize > max_KS :
        return None;
    WK=math.floor(math.log2(scipy.special.comb(n, t, exact=True)/scipy.special.comb(n-k, t, exact=True)));
    if WK < min_WK :
        return None;
    return [n,s,k,t,WK,KeySize];

RES=[]
for s in range(min_s,max_s) :
    if e_min !=e_max :
        res=[]
        n_min=math.floor(nbpts*e_min)
        n_max=math.floor(nbpts*e_max)
        for i in range(n_max,n_min,-200):
            if i <= nbpts-s :
                l=Study(i,s);
                if l != None:
                    res.append(l);
        if res != [] :
            RES.append(res)
    else:
        l=Study(n,s);
        if l != None :
            RES.append(l);

print("Nombre de solutions:" + str(len(RES)))

if len(RES) !=0:
    if e_min !=e_max :
        RES2 = [item for sublist in RES for item in sublist]
    else:
        RES2 = RES;
        
    minval = min(x[5] for x in RES2)
    best=[x for x in RES2 if x[5]==minval]
    print(best)
