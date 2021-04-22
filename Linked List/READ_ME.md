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

### Linked List Traversal
```
// A simple C++ program for traversal of a linked list
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Node
{
	public:
		int data;
		Node* next;
 };
 
// This function prints contents of linked list
// starting from the given node
void printList(Node* n)
{
	while (n!=NULL)
	{
		cout << n->data << " ";
		n = n->next;
	}
}

int main()
{
	Node* head = NULL;
	Node* second = NULL;
	Node* third = NULL;
	
	head = new Node();
	second = new Node();
	third = new Node();
	
	head->data = 1;
	head->next = second;
	
	second->data = 2;
	second->next = third;
	
	third->data = 3;
	third->next = NULL;
	
	printList(head);
	return 0;
```
### Insertion
A node can be added in three ways:
1) At the front of the linked list
2) After a given node
3) At the end of the linked list

#### Add a node at the front
The new added node will become the new head of the linked list. For example, the given linked list is 10->15->20->25, we add an item 5 a the front of the linked list. Let us call the function that add a node at the front of the linked list **push()**. 
1) Cut the head pointer point to the old first element.
2) head points to the new first element, which is 5.
3) link the first new element 5 to the old first element, which is 10

```
# This is Python code
# This function is in LinkedList class
# Function to insert a new node at the beginning
def push(self, new_data):
	new_node = Node(new_data)
	new_node.next = self.head
	self.head = new_node
	
```

```
# This is C++ code
/* Given a reference (pointer to pointer) 
to the head of a list and an int, 
inserts a new node on the front of the list. */
void push(Node** head_ref, int new_data)
{
	/* 1. allocate node */
	Node* new_node = new Node();
	
	/* 2. put in the data */
	new_node->data = new_data;
	
	/* 3. Make next of new node as head */
	new_node->next = (*head_ref);
	
	 /* 4. move the head to point to the new node */
	(*head_ref) = new_node;
}
```
Time complexity of push() is O(1).

#### Add a node after a given node
We are given pointer to a node, and the new node is inserted after the given node.

```
// Given a node prev_node, insert a 
// new node after the given prev_node
void insertAfter(Node* prev_node, int new_data)
{
	//1. Check if the given prev_node is NULL
	if (prev_node == NULL)
	{
		cout << "the given previous node cannot be NULL" << endl;
		return ;
	}
	
	// 2. Allocate new node
	Node* new_node = new Node();
	
	// 3. Put in the data
	new_node->data = new_data;
	
	// 4. Make next of new node as next of prev_node
	new_node->next = prev_node->next;
	
	// 5. move the next of prev_node as new_node;
	prev_node->next = new_node;
}
```
For Python code
```
# This function is in LinkedList class. 
# Inserts a new node after the given prev_node. This method is 
# defined inside LinkedList class shown above 
def insertAfter(self, prev_node, new_data):
	# 1. check if the given prev_node exists
	if prev_node is None:
		print("The given previous node must be in linked list.")
		return 
	# 2. Create new node & 3. Put in the data
	new_node = Node(new_data)
	
	# 4. Make next of new Node as next of prev_node
	new_node.next = prev_node.next
	
	# 5. Make next of prev node as new_node
	prev_node.next = new_node
```
Time complexity of insertAfter() is O(1).

#### Add a node at the end
The new node is always added after the last node of the given linked list.
Since a linked list is typically represented by the head of it, we have to traverse teh list till end and then change the next of last node to the new node.
For C++ code
```
// Given a reference (pointer to pointer) to the head  
// of a list and an int, appends a new node at the end 
void append(Node** head_ref, int new_data)
{
	// 1. allocate node
	Node* new_node = new Node();
	
	// Used in step 5
	Node* last = *head_ref;
	
	// 2. Put in the data
	new_node->data = new_data
	
	// 3. This new node is going to be the last node, 
	so make next of it as NULL
	new_node->next = NULL
	
	// 4. If the linked list is empty,
	// then make the new node as head
	if (*head_ref == NULL)
	{
		*head_ref = new_node;
		return ;
	}
	
	// 5. Else traverse till the last node
	while (last->next != NULL)
		last = last->next;
		
	// 6. Change the next of the last node
	last->next = new_node;
	return ;
}
```
For Python code
```
def append(self, new_data):
	# 1 & 2: Allocate the Node &
        # Put in the data
	# 3. Set next as None
	new_node = Node(new_data)
#	new_node.next = None
	 # 4. If the Linked List is empty, then make the
         # new node as head
	if self.head is None:
		self.head = new_node
		return
	
	# 5. Else traverse till the last node
	last = self.head
	while (last.next):
		last = last.next
		
	# 6. Change the next of last node
	last.next = new_node
	
```
Time complexity of append is O(n) where n is the number of nodes in linked list

	
### Deleting a node
Given a 'key', delete the first occurence of this key in the linked list.

#### Iterative method:
1. Find the previous node of the node to be deleted.
2. Change the next of the previous node
3. Free memory for the node to be deleted.

```
// Given a reference (pointer to pointer)
// to the head of a list and a key, deletes
// the first occurrence of key in linked list
void deleteNode(Node** head_ref, int key)
{
	// Store head node
	Node* temp = *head_ref;
	Node* prev = NULL;
	
	// If head node itself holds 
	// the key to be deleted
	if (temp != NULL && temp->data == key)
	{
		*head_ref = temp->next;
		delete temp;
		return ;
	}
	
	// Else Search for the key to be deleted,
	// keep track of the previous node as we
	// need to change 'prev->next';
	else
	{
		while (temp!= NULL && temp->data != key)
		{
			prev = temp;
			temp = temp->next;
		}
		if (temp == NULL)
			return ;
			
		prev->next = temp->next;
		delete temp;
		
	}	
}
```

### Delete a linked list node at a given position
Given a singly linked list and a position, delete a linked list node at the given position.

```
void deleteNode(Node **head_ref, int position)
{
	if (*head_ref == NULL)
		return;
	// Store head node
	Node* temp = *head_ref
	
	if (position == 0)
	{
		*head_ref = temp->next;
		// free old head
		free(temp)
		return ;
	}
	
	for (int i=0; temp != NULL & i < position-1)
	{
		temp = temp->next;
	}
	
	if (temp == NULL || temp->next == NULL)
		return ;
	
	Node *next = temp->next->next;
	
	free(temp->next);
	temp->next = next;
}
```

### Write a function to delete a linked list
Algorithms for C/C++: Iterate through the 

