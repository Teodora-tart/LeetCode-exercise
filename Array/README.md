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
  
  This is C++ Code:
  ```
  class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int max_area = 0;
        int area;
        while (left < right)
        {
            area = (right-left)*(height[left]<height[right] ? height[left]:height[right]);
            if (area > max_area)
                max_area = area;
            
            if (height[left]<=height[right])
                left++;
            else if (height[left]>height[right])
                right--;
        }
        
        return max_area;
    }
};
```
## Search in Rotated Sorted Array
```
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
```
My thoughts: binary search 
find the pivot point -> determine the target belongs to the 'left side' of the array or the 'right side'
See my attached code.

Here is a more advanced code, which lists the situation that the target belongs to the left or right side.


## Search in Rotated Sorted Array II
```
Follow up for ”Search in Rotated Sorted Array”: What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Write a function to determine if a given target is in the array
```
My first thought is very brute force, reduce the duplicated sorted array into non-duplicated sorted array and then use algorithms in the last question.


## Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```
My first thought: using sorted array, the time complexity is O(nlogn)
However, the problem asks: "Could you implement the O(n) solution?"

I attached my naive solution inspired by hash map:
```
def longestConsecutive(nums):
    nums = set(nums)
    consecutive = {}

    for num in nums:
        if num+1 not in nums:
            consecutive[num] = num
        else:
            yy = num + 1     
            while yy in nums:
                yy += 1
            consecutive[num] = yy
    
    largest = 0
    for key, values in consecutive.items():
        key = int(key)
        largest = max(largest, values - key)
    return largest
 ```
 Also, I uploaded the advanced solution in the folder
 
## May 3th
## Remove Element:
'''
Given an array and a value, remove all instances of that value in place and return the new length.
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3]
Explanation: Your function should return length = 5, with the first five elements of nums 
containing 0, 1, 3, 0, and 4. Note that the order of those five elements can be arbitrary. 
It doesn't matter what values are set beyond the returned length.
'''
Very easy to solve, so I omit the procedure

## Next Permutation
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation
of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.
'''
I found it hard to understand, but when I saw this picture, it is not hard to understand and easy to write the code following the steps on the picture.

<img width="532" alt="nextPermutation" src="https://user-images.githubusercontent.com/82644032/116847158-9099ea80-ac1c-11eb-893e-e350cebd463b.png">

