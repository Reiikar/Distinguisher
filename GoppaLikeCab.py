# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:52:45 2023

@author: jade

étude Goppa-like Hermitien
"""

import scipy.special
import math

q=2;
m=12;
a=2;
b=1;
assert  math.gcd(a,b) == 1;
g=(a-1)*(b-1)//2;
#On va se permettre de faire varier la longueur entre e*q0^3 et q0^3 pour 0<e<=1 
 #Fraction du nombre de points rationels total qu'on évalue
e_min=0.5;
e_max=1
n=q**m+2*g*math.floor(math.sqrt(q**m));



min_t=64; #Le minimum d'erreurs qu'on veut décoder
min_WK=142; #La sécurité minimum acceptée
max_KS= 3*10**6#Taille de clé maximum

min_s= min_t;
max_s=n;

def Study(n,s):
    k=n-m*(s-g+1);
    if k <=0 :
        #print("Pb dimension!")
        return None;
    t=s;
    if t < min_t :
        return None;
        print("Pb correction!")
    KeySize= math.floor(math.log2(q)*k*(n-k))
    if KeySize > max_KS :
        print("Pb KS!")
        return None;
    WK=math.floor(math.log2(scipy.special.comb(n, t, exact=True)/scipy.special.comb(n-k, t, exact=True)));
    if WK < min_WK :
        print("Pb WK! " + str(WK) )
        return None;
    return [n,s,k,t,WK,KeySize];

RES=[]
for s in range(min_s,max_s) :
    if e_min !=e_max :
        n_min=math.floor(n*e_min)
        n_max=math.floor(n*e_max)
        step=math.floor((n_max-n_min)/10);
        res=[]
        for i in range(n_max,n_min,-step):
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
