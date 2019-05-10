# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:27:22 2019

@author: Lavi
"""
def maximumsumsubarray(ar,size):
    max_so_far=ar[0]
    curr_max=ar[0]
    for i in range(1,size):
        curr_max=max(ar[i],curr_max+ar[i])
        max_so_far=max(max_so_far,curr_max)
    return max_so_far




ar=[-2,-3,4,-1,-2,1,5,-3]
n=len(ar)
print(maximumsumsubarray(ar,n))