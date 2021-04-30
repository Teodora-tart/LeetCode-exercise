# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 22:36:38 2021

@author: Song Yifan
"""

def binary_search(target, lst):
    right = len(lst)
    left = 0
    middle = (left+right)//2
    while left < right:
        if lst[middle] == target:
            return middle
        elif lst[middle] < target:
            left = middle
        elif lst[middle] > target:
            right = middle
        middle = (left + right)//2
    return -1

def find_pivot(nums):
    right = len(nums)
    left = 0
    mid = (left + right)//2
    while left < right:
        if nums[mid-1] < nums[mid] < nums[mid+1]:
            left = mid
            mid = (left+right)//2
        elif nums[mid] < nums[mid-1]:
            pivot = mid
            break
        elif nums[mid] > nums[mid+1]:
            pivot = mid+1
            break
    return pivot

def search(target, nums):
    pivot = find_pivot(nums)
    if nums[pivot] == target:
        return pivot
    else:
        if target > nums[len(nums)-1]:
            return binary_search(target, nums[:pivot])
        else:
            res = binary_search(target, nums[pivot:])
            if res != -1:
                return res + pivot
            else:
                return res

print(search(5, [4,5,6,7,0,1,2]))