# Linked List
I think before I start, I have to revise linked-list before I start.
## Revision of Linked List
### Introduction
elements are linked with pointers.

### Why Linked list?
Arrays can be used to store linear data of similar types, but arrays have the following limitations.
1) The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.
2) Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted.
### Advantages over arrays
1) Dynamic size
2) Ease of insertion/deletion
### Drawbacks
1) Random access is not allowed. have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists efficiently with its default implementation. 
2) Extra memory space for a poiter is required with each element of the list
3) Not cache friendly.Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.

### Representation
A linked list is represented by a pointer to the first node of the linked list. The first node is called the head. If the linked list is empty, then the value of the head is NULL.
Each node in a list consists of at least two parts:
1) data
2) Pointer (Or Reference) to the next node

In C++
```
class Node
{
    public:
      int data;
      Node* next;
};
```
In Python
```
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None  # Initialize next as null
    
class LinkedList:
  # Function to initialize the linked List object
  def __init__(self):
    self.head = None
```

### Simple Linked List in C++
```
using namespace std;
 
class Node
{
    public:
      int data;
      Node* next;
};

// Program to create a simple linked
// list with 3 nodes
int main()
{
	Node* head = NULL;
	Node* second = NULL;
	Node* third = NULL;
	
	// allocate 3 nodes in the heap
	head = new Node();
	second = new Node();
	third = new Node();
	
	/* Three blocks have been allocated dynamically. 
    We have pointers to these three blocks as head, 
    second and third    
    
     head         second         third 
        |             |             | 
        |             |             | 
    +---+-----+     +----+----+     +----+----+ 
    | # | # |     | # | # |     | # | # | 
    +---+-----+     +----+----+     +----+----+ 
      
	# represents any random value. 
	Data is random because we haven’t assigned 
	anything yet */
	
	head->data = 1; //assign data in first node
	head->next = second; // Link first node to the second node
	/* data has been assigned to the data part of first 
    block (block pointed by the head). And next 
    pointer of the first block points to second. 
    So they both are linked. 
  
    head         second         third 
        |             |             | 
        |             |             | 
    +---+---+     +----+----+     +-----+----+ 
    | 1 | o----->| # | # |     | # | # | 
    +---+---+     +----+----+     +-----+----+     
	*/
	
	// assign data to second node
	second->data = 2;
	
	// Link second node with the third node
	second->next = third;
	 /* data has been assigned to the data part of the second 
    block (block pointed by second). And next 
    pointer of the second block points to the third 
    block. So all three blocks are linked. 
      
    head         second         third 
        |             |             | 
        |             |             | 
    +---+---+     +---+---+     +----+----+ 
    | 1 | o----->| 2 | o-----> | # | # | 
    +---+---+     +---+---+     +----+----+     */
    third->data = 3;
    third->next = NULL;
    /* data has been assigned to the data part of the third 
    block (block pointed by third). And next pointer 
    of the third block is made NULL to indicate 
    that the linked list is terminated here. 
  
    We have the linked list ready. 
  
        head     
            | 
            | 
        +---+---+     +---+---+     +----+------+ 
        | 1 | o----->| 2 | o-----> | 3 | NULL | 
        +---+---+     +---+---+     +----+------+     
      
      
    Note that only the head is sufficient to represent 
    the whole list. We can traverse the complete 
    list by following the next pointers. */
    return 0;
  
}
```
