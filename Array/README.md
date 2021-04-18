# LeetCode-exercise
This is a notebook for myself to practice LeetCode algorithm problems. I will use Python (which is familiar to me) and C++ (I will try to practice more) to write code.

## Array
### Easy: Two Sums
Given a list only containing integers, return the index of two numbers whose sum equals to the target.
Assume for every input, there is only one answer, and there won't be repeating numbers.
> Example:
>> Given nums = [2,7,11,15], target = 9
>> Because nums[0]+nums[1] = 2+7 = 9
>> returns [0,1]

### My thoughts:
First, the most naive methods, for-loop every elements.
```
# This is Python Code
result = []
for i in range(len(nums)-1):
  for j in range(i, len(nums)):
    if nums[i] + nums[j] == target:
      result.append(i)
      result.append(j)
 ```
 However, the time complexity for this method is O(n^2). Will think about quicker solution.

I first think of using the sorted array, and find the proper position for the target,i.e., all the elements on the left hand side of the target is smaller than target and elements on the right hand side of the target is bigger than the target. Then I only have to search for the left side. However, I find later that the time complexity is still O(n^2). 

I then read *Jack-Cherish*'s solution. Every brilliant solution uses dictionary in Python.
For each element, it uses dictionary to store the corresponding element (i.e., sum of this two elements equal to target value) as the key and index of the original element as value. When looping the array, if the element afterwards is in dictionary, and it's what we want.

```
def solution(nums, target):
  result = {}
  for i in range(len(nums)):
      if nums[i] in result:
          return [result[nums[i]],i]
      else:
          result[target-nums[i]] = i
```
          
### Medium:
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

My naive-thoughts:
loops, time complexity O(n^2)
#### Brute-Force method
```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(height)-1):
            for j in range(i, len(height)):
                area = min(height[i],height[j])*(j-i)
                if area > max_area:
                    max_area = area
        return max_area
```
However, takes too long to run. Have to advance.
#### Two pointer approach
The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. Further, the farther the lines, the more will be the area obtained.
so I first select the leftmost and rightmost lines, compare the height of two lines, if left line is shorter, I move inward from left to find whether there is longer line. Similar for the other side. 

```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        n = len(height)
        left = 0
        right = n-1
        while left < right:
            area = min(height[left], height[right])*(right-left)
            if area > max_area:
                max_area = area
            if height[left] <= height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_area
 ```
  
