# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:02:28 2019

@author: Lavi
"""
def leader(ar,size):
    max=ar[size-1]
    print(max,end=' ')
    for i in range(size-2,0,-1):
        if(max<ar[i]):
            print(ar[i],end=' ')
            max=ar[i]
         
    
ar=[16,17,4,3,5,2]
size=len(ar)
leader(ar,size)