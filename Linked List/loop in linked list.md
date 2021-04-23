# Detect loop in a linked list
Given a linked list, check if the linked list has loop or not.
## Solution 1: Hashing approach
Traverse the list one by one and keep putting the node addresses in a Hash Table. At any point, if NULL is reached then return false and if next of current node points to any of the previously stored nodes in Hash then return true. 
```
#include <bits/stdc++.h>
using namespace std;

struct Node
{
  int data;
  struct Node *next;
 }
;

bool detectLoop(struct Node *h)
{
  unordered_set<Node*> s;
  while (h != NULL)
  {
    if (s.find(h) != s.end())
      return true;
    s.insert(h);
    h = h->next;
  }
  return false;
 }
 ```
 Time complexity: O(n) 
 Auxiliary Space: O(n)
 
 ## Solution 2:
 Approach: This solution requires modifications to the basic linked list data structure. 
 * Have a visited flag with each node
 * Traverse the linked list and keep marking visited node
 * If you see a visited node again then there is a loop. This solution works in O(n) but requires additional information with each node.
 * A variation of this solution that doesn’t require modification to basic data structure can be implemented using a hash, just store the addresses of visited nodes in a hash and if you see an address that already exists in hash then there is a loop.
```
#include <bits/stdc++.h>
using namespace std;

struct Node
{
  int data;
  struct Node* next;
  int flag;
};

void push(struct Node** head_ref, int new_data)
 {
    struct Node* new_node = new Node();
    new_node->data = new_data;
    new_node->flag = 0;
    
    new_node->next = (*head_ref);
    
    (*head_ref) = new_node;
 }
 
 bool detectLoop(struct Node* h)
 {
    while(h != NULL)
    {
      if (h->flag == 1)
        return true;
      h->flag = 1;
      h = h->next;
    }
    return false;
 }
 
 ```
 Time complexity: O(n)
 Auxiliary Space: O(1)
 
## Solution 3: Floyd's Cycle-Finding Algorithm
Approach: This is the fastest method and has been described below:  
Traverse linked list using two pointers.
Move one pointer(slow_p) by one and another pointer(fast_p) by two.
If these pointers meet at the same node then there is a loop. If pointers do not meet then linked list doesn’t have a loop.
```
#include <bits/stdc++.h>
using namespace std;

class Node
{
    public:
      int data;
      Node* next;
};

int detectLoop(Node* list)
{
  Node *slow_p = list, *fast_p = list;
  while (slow_p && fast_p && fast_p->next)
  {
      slow_p = slow_p->next;
      fast_p = fast_p->next;
      if (fast_p == slow_p)
        return true;
  }
    return 0;
  }
  ```
  
  
