# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:38:30 2019

@author: Lavi
"""
# Python code to demonstrate 
# sort list by frequency 
# of elements 

from collections import Counter

ini_list = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8] 

# printing initial ini_list 
print ( ini_list) 

# sorting on bais of frequency of elements 

result = [item for items, c in Counter(ini_list).most_common() 
									for item in [items] * c] 
# printing final result 
print("final list", (result)) 
