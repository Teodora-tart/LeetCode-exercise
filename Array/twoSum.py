# -*- coding: utf-8 -*-
"""
Created on Sun May  2 14:11:45 2021

@author: Song Yifan
"""

# Given an array of integers, find two numbers such that 
# they add up to a specific target number
def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic.keys():
            return dic[nums[i]],i
        else:
            dic[target-nums[i]] = i
            
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
