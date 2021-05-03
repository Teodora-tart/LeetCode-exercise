# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:52:38 2021

@author: Song Yifan
"""

'''
Given an array and a value, remove all instances of that value in place and return the new length.
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3]
Explanation: Your function should return length = 5, with the first five elements of nums 
containing 0, 1, 3, 0, and 4. Note that the order of those five elements can be arbitrary. 
It doesn't matter what values are set beyond the returned length.
'''

def removeElement(nums, val):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index



























