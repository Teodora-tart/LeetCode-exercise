# Seach in a Linked List 
## search an element in a linked list.
Write a function that searches a given key ‘x’ in a given singly linked list. The function should return true if x is present in linked list and false otherwise.
```
bool search(Node *head, int x)
```

### Iterative Solution
2) Initialize a node pointer, current = head
3) Do following while current is not NULL
> a) current->key is equal to the key being searched return true
> b) current = current->next
5) Return False


### Recursive Solution
```
bool search(head, x)
1) If head is NULL, return false
2) If head's key is the same as x, return true;
3) else return search(head->next, x)
```
## Write a function to get Nth node in a linked list
Write a GetNth() function that takes a linked list and an integer index and returns the data value stored in the node at that index position. 
### Algorithm
```
1. Initialize count = 0
2. Loop through the linked list
3. if count is equal to the passed index then return current node
4. increment count
5. change current to point to next of the current
```
### Method2 - With Recursion
#### Algorithm
```
getNth(node, n)
1. Initialize count = 0
2. if count == n
      return node-> data
3. else: return getNth(node->next, n-1)
```
## n’th node from the end of a Linked List
### Method 1 (Use length of linked list)
1)  Calculate the length of Linked List. Let the length be len. 
2)  Print the (len – n + 1)th node from the beginning of the Linked List. 
Time complexity: O(n)

### Method 2 (Use two pointers)
Double pointer concept : First pointer is used to store the address of the variable and second pointer used to store the address of the first pointer. If we wish to change the value of a variable by a function, we pass pointer to it. And if we wish to change value of a pointer (i. e., it should start pointing to something else), we pass pointer to a pointer.

Time Complexity: O(n) where n is the length of linked list.

## Find the middle of a given linked list
### Method 1:
Traverse the whole linked list and count the no. of nodes. Now traverse the list again till count/2 and return the node at count/2. 

### Method 2:
Initialize mid element as head and initialize a counter as 0. Traverse the list from head, while traversing increment the counter and change mid to mid->next whenever the counter is odd. So the mid will move only half of the total length of the list. 
```
using namespace std;

struct Node
{
	int data;
	struct node* next;
};

void printMiddle(struct node* head)
{
	int count = 0;
	struct node *mid = head;
	
	while (head != NULL)
	{
		if (count&1)
			mid = mid->next;
		count++;
		head = head->next;
	}
	
	if (mide != NULL)
		printf("The middle element is [%d]\n\n",
				mid->data);
}
```
