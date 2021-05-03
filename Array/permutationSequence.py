# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:48:03 2021

@author: Song Yifan
"""
from math import factorial

def getPermutation(n, k):
    string = ''
    total = n
    lst = [i for i in range(1,n+1)]
    k = k-1
    while (n > 0):
        index, k = divmod(k, factorial(n-1))
        string += str(lst[index])
        n = n-1
        lst.remove(lst[index])
    return string

print(getPermutation(4,9))
    
        
        
        
        
        
    
    