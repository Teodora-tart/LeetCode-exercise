# -*- coding: utf-8 -*-
"""
Created on Sun May  2 14:32:45 2021

@author: Song Yifan
"""

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0
'''
import itertools

def twoSum(nums, target):
    dic = {}
    sol = []
    if len(nums) == 0:
        return 
    for num in nums:
        if num in dic.keys():
             sol.append([dic[num],num])
        else:
            dic[target-num] = num
    return sol
            
def threeSum(nums):
    solution = []
    buffer = {}
    for i in range(len(nums)):
        buffer[i] = -nums[i] 
    
    for key, val in buffer.items():
        if key <= len(buffer)-2:
            if twoSum(nums[key+1:], val):
                for x in twoSum(nums[key+1:], val):
                    j, k = x[0], x[1]
                    solution.append([-val, j, k])
                    
    s = [sorted(k) for k in solution]
    s.sort()
    sols = list(s for s, _ in itertools.groupby(s))
   
    return sols

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

        
    