# Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.
class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        maxLength = 0
        for num in nums:
            if num-1 not in nums:
                n = num + 1
                while n in nums:
                    n = n+1
                maxLength = max(maxLength, n-num)
        return maxLength

                
