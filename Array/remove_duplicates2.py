# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:42:56 2021

@author: Song Yifan
"""

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    for n in nums:
        if i<2 or n>nums[i-2]:
            nums[i] = n
            i += 1
    return i

nums = [1,1,1,2,2,3,3]
print(removeDuplicates(nums))        
                
                
                