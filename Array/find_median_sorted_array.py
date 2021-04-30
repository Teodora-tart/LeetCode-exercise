# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:59:39 2021

@author: Song Yifan
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        sorted_array = []
        i,k = 0, 0
        while (i<m) and (k<n):                
            if nums1[i] <= nums2[k]:
                sorted_array.append(nums1[i])
                i += 1
            else:
                sorted_array.append(nums2[k])
                k += 1
        if (i == m):
            sorted_array.extend(nums2[k:])
        if (k == n):
            sorted_array.extend(nums1[i:])
            
        if (m+n)%2 == 1:
            return sorted_array[(m+n)//2]
        else:
            return (sorted_array[(m+n)//2-1]+sorted_array[(m+n)//2])/2
                    
#%%
def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        sorted_array = []
        i,k = 0, 0
        while (i<m) and (k<n):                
            if nums1[i] <= nums2[k]:
                sorted_array.append(nums1[i])
                i += 1
            else:
                sorted_array.append(nums2[k])
                k += 1
        if (i == m):
            sorted_array.extend(nums2[k:])
        if (k == n):
            sorted_array.extend(nums1[i:])
        
        if (m+n)%2 == 1:
            return sorted_array[(m+n)//2]
        else:
            return (sorted_array[(m+n)//2-1]+sorted_array[(m+n)//2])/2

print(findMedianSortedArrays([1,2], [3,4]))
            

                