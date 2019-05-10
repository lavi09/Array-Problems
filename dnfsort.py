# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:27:30 2019

@author: Lavi
"""
def dnfsort(ar,n):
    low=0
    high=n-1
    mid=0
    while(mid<=high):
        if ar[mid]==0:
            ar[low],ar[mid]=ar[mid],ar[low]
            low+=1
            mid+=1
        elif ar[mid]==1:
            mid+=1
        else:
            ar[mid],ar[high]=ar[high],ar[mid]
            high-=1
    return ar

ar=[0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n=len(ar)
print(dnfsort(ar,n))
