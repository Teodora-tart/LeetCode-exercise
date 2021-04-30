# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 09:42:38 2021

@author: Song Yifan
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return True
            if nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[low] > nums[mid]:
                if nums[mid]<= target < nums[len(nums)-1]:
                    low = mid + 1
                else:
                    high = mid - 1
            else: low += 1   # Tricky part: for the case when nums[low] == nums[mid]
        return False
    
                    


    
                        