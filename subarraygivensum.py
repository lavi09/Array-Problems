# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:25:27 2019

@author: Lavi
"""
def subarraysum(arr,n,sum):
    curr_sum=arr[0]
    start=0
    i=1
    while(i<=n):
        while curr_sum > sum and start < i-1 :
            curr_sum-=arr[start]
        start+=1
        if(curr_sum==sum):
            print('Index',i-1, 'to', start)
            return 1
        if i<n:
            curr_sum+=arr[i]
        i+=1
    print ("No subarray found")
    return 0
            
            







arr=[1,2,3,4,5,6,7,8,9]
sum=20
n=len(arr)
subarraysum(arr,n,sum)