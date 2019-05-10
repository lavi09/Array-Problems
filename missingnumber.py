# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:46:01 2019

@author: Lavi
"""
def missingnumber(ar,n):
    
    actualsum=0
    expectedsum=int((pow(n,2)+n)/2)

    for i in range(0,n-1):
        actualsum+=ar[i]
    print(actualsum)
    return expectedsum-actualsum
    
ar=[1,2,3,4,5,6,7,9,10]
n=len(ar)

print(missingnumber(ar,n+1))