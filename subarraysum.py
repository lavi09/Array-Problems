# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:58:44 2019

@author: Lavi
"""
def subArraySum(arr, n, Sum):  
   
    # create an empty map  
    Map = {}  
    
    # Maintains sum of elements so far  
    curr_sum = 0 
    
    for i in range(0,n):  
       
        # add current element to curr_sum  
        curr_sum = curr_sum + arr[i]  
        
        # if curr_sum is equal to target sum  
        # we found a subarray starting from index 0  
        # and ending at index i  
        if curr_sum == Sum:  
           
            print("Sum found between indexes 0 to", i) 
            
           
        print(curr_sum-Sum)
        # If curr_sum - sum already exists in map  
        # we have found a subarray with target sum  
        if (curr_sum - Sum) in Map:  
            
            print("Sum found between indexes",Map[curr_sum - Sum] + 1, "to", i)  
              
            return 1
    
        Map[curr_sum] = i  
        print("m",Map[curr_sum])
    # If we reach here, then no subarray exists  
    print("No subarray with given sum exists")  
   
    
# Driver program to test above function  
if __name__ == "__main__":  
   
    arr = [10,2,-2,-20,10]  
    n = len(arr)  
    Sum = -10
    
    
    subArraySum(arr, n, Sum)  