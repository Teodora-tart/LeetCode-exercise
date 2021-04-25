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
  
  Time complexity: O(n)
  Auxiliary Space: O(1)

## Detect and Remove Loop in a Linked List

### Method 1: Check one by one
We know that Floyd’s Cycle detection algorithm terminates when fast and slow pointers meet at a common point. We also know that this common point is one of the loop nodes (2 or 3 or 4 or 5 in the above diagram). Store the address of this in a pointer variable say ptr2. After that start from the head of the Linked List and check for nodes one by one if they are reachable from ptr2. Whenever we find a node that is reachable, we know that this node is the starting node of the loop in Linked List and we can get the pointer to the previous of this node.

```
#include<bits/stdc++.h>
using namespace std;

struct Node{
  int data;
  struct Node* next;
 };
 
 void removeLoop(struct Node*, struct Node*);
 
 int detectAndRemoveLoop(struct Node* list)
 {  
    struct Node *slow_p = list, *fast_p = list;
    while (slow_p && fast_p && fast_p->next)
    {
        slow_p = slow_p->next;
        fast_p = fast_p->next->next;
        if (fast_p == slow_p)
        { 
            removeLoop(slow_p, list);
            return 1;
         }
     }
    
      return 0;
    }
 
 void removeLoop(struct Node* loop_node, struct Node* head)
 {  
    struct Node* ptr1;
    struct Node* ptr2;
    /* Set a pointer to the beginning
      of the Linked List and
      move it one by one to find the
      first node which is
      part of the Linked List */
     ptr1 = head;
     while (1) {
        /* Now start a pointer from
        loop_node and check if
       it ever reaches ptr2 */
       ptr2 = loop_node;
       while (ptr2->next != loop_node
       && ptr2->next != ptr1)
       {
          ptr2 = ptr2->next;
       }
       
        /* If ptr2 reahced ptr1
        then there is a loop. So
        break the loop */
        if (ptr2->next == ptr1)
          break;
          
         ptr1 = ptr1->next;
    }
        ptr2->next = NULL;
 }
 
 ```
 
 ### Method 2
 1. This method is also dependent on Floyd's Cycle detection algorithm
 2. Detect Loop using Floyd's Cycle detection algorithm and get the pointer to a loop node.
 3. Count the number of nodes in loop. Let the count be k.
 4. Fix on pointer to the head and another to a kth node from the head.
 5. Move both pointers at the same pace, they will meet at loop starting node.
 6. Get a pointer to the last node of the loop and make next of it as NULL
![delete loop](https://user-images.githubusercontent.com/82644032/115984526-0f1dd900-a5da-11eb-8f5d-42a4853b6c67.jpg)

### Method 3
We do not need to count number of nodes in Loop. After detecting the loop, if we start slow pointer from head and move both slow and fast pointers at same speed until meet, they would meet at the beginning of the loop.
![deleteloop1](https://user-images.githubusercontent.com/82644032/115984766-5c4e7a80-a5db-11eb-8397-ddfd124216b5.jpg)

 
