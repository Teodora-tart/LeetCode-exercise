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
