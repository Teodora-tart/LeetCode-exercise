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
          
      
      
