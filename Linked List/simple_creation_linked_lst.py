# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 20:40:41 2021

@author: Song Yifan
"""

# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None
        

# Linked List Class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None

# Code execution starts here
if __name__ == '__main__':
    llist = LinkedList()
    
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''
    
    llist.head.next = second # Link first node with second
    '''
    Now next of first Node refers to second.  So they
    both are linked.
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''
    second.next = third # Link second node with the third node
  
    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''
    
    