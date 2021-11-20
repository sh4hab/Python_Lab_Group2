# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 00:37:46 2021

@author: MohammadAmin
"""

def cost(N, D, P, F, C, d):
    if F*d<=C:
        return C-d*F,0
    elif N==0:
        return -1,-1
    else:
        costt=max(P)*F*d
        for i in range(N):
            if(d-D[i]<=C/F):
                t=cost(i, D[0:i], P[0:i], F, C, D[i])
                if t[0]>=0:
                    if(t[1]+(C-t[0])*P[i]<costt):
                        costt=t[1]+(C-t[0])*P[i]
                        remain=C-(d-D[i])*F
        if costt<max(P)*F*d:
            return remain,costt  
        else: 
            return -1,-1           
            
 
print(cost(0,[],[],1,20,125))#UNREACHABLE
#RECURSIVE BASE
print(cost(0,[],[],1,20,15)) 
print(cost(1,[10],[2],1,20,15))
#EXMPLE CHANGING COSTS
print(cost(2,[5 ,15],[3,0.9],1,20,25))
print(cost(2,[5 ,15],[1,3],1,20,25))
#MORE EXAMPLES
print(cost(3,[20 ,40,60],[2,2,2],1,20,80))
print(cost(3,[20 ,40,61],[2,2,2],1,20,60))