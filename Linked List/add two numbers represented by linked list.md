# Add two numbers represented by linked lists
## Example
> Input:
> 
> List 1: 5->6->3 // represents number 365 
>
> List 2: 8->4->2  // represents number 248 
> 
> Output: Resultant list: 3->1->6 // represents number 613 
> 
> Explanation: 365 + 248 = 613

## Add two numbers represented by linked lists version 2
Given two numbers represented by two linked lists, write a function that returns the sum list. The sum list is linked list representation of the addition of two input numbers. It is not allowed to modify the lists. Also, not allowed to use explicit extra space (Hint: Use Recursion).

### Method:
1. Calculate sizes of given two linked list.
2. If sizes are the same, then calculate sum using recursion. Hold all nodes in recursion call stack till te rightmost node, calculate the sum of rightmost nodes and forward carry to th left side
3. If size is not the same, then follow below steps:
 a) Calculate difference of sizes of two linked lists. Let the difference be diff 
 b) Move diff nodes ahead in the bigger linked list. Now use step 2 to calculate the sum of the smaller list and right sub-list (of the same size) of a larger list. Also, store the carry of this sum. 
 c) Calculate the sum of the carry (calculated in the previous step) with the remaining left sub-list of a larger list. Nodes of this sum are added at the beginning of the sum list obtained the previous step.
 
