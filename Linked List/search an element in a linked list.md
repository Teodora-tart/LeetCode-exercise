# Seach an element in a Linked List (Iterative and Recursive)
Write a function that searches a given key ‘x’ in a given singly linked list. The function should return true if x is present in linked list and false otherwise.
```
bool search(Node *head, int x)
```

## Iterative Solution
2) Initialize a node pointer, current = head
3) Do following while current is not NULL
> a) current->key is equal to the key being searched return true
> b) current = current->next
5) Return False


## Recursive Solution
```
bool search(head, x)
1) If head is NULL, return false
2) If head's key is the same as x, return true;
3) else return search(head->next, x)
```
