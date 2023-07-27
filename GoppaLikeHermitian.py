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
e=0; #Le nombre de points qu'on enlève pour évaluer
n=q0**3-e;

min_t=84; #Le minimum d'erreurs qu'on veut décoder
min_WK=142; #La sécurité minimum acceptée
min_s= 2*min_t+2*g-2;
max_s=n

RES=[]
for s in range(min_s,max_s) :
    k=n-m*(s-g+1);
    if k <=0 :
        break
    t=s//2-g+1;
    WK=math.floor(math.log2(scipy.special.comb(n, t, exact=True)/scipy.special.comb(n-k, t, exact=True)));
    if WK >= min_WK :
        KeySize= math.floor(math.log2(q)*k*(n-k))
        RES.append([s,k,t,WK,KeySize])

