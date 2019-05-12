# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:15:56 2019

@author: Lavi
"""
import random
def quickselect(arr, k):
    '''
     k = 1 returns first element in ascending order.
     can be easily modified to return first element in descending order
    '''

    r = random.randrange(0, len(arr))
    print(r)

    a1 = [i for i in arr if i < arr[r]]
    print(a1)
    a2 = [i for i in arr if i > arr[r]]
    print(a2)

    if k <= len(a1):
        return quickselect(a1, k)
    elif k > len(arr)-len(a2):
        return quickselect(a2, k - (len(arr) - len(a2)))
    else:
        return arr[r]
ar=[7,10,4,3,20,15]
k=2
print(quickselect(ar,k))