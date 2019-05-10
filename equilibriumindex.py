# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:17:47 2019

@author: Lavi
"""
def equilibriumindex(ar,n):
    total=sum(ar)
    left_sum=0
    for i in range(0,n):
        total-=ar[i]
        if left_sum==total:
            return i
        left_sum+=ar[i]
    




ar=[-7,1,5,2,-4,3,0]
n=len(ar)
print(equilibriumindex(ar,n))