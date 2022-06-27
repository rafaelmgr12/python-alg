#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    # Write your code here
    # create a new node
    new_node = DoublyLinkedListNode(data)
    # case 1: list is empty
    if llist is None:
        llist = new_node

    # case 2: insert before the head
    elif data < llist.data:
        new_node.next = llist
        llist.prev = new_node
        llist = new_node
    # case 3: insert at a specific position or at the ends
    else:
        cur = llist
        #tranverse to the specicifc positon
        while cur.next is not None and cur.next.data < data:
            cur = cur.next
        # insert at the end
        if cur.next is None and cur.data < data:
            cur.next = new_node
            new_node.prev = cur
        else:
            new_node.next = cur.next
            new_node.prev = cur
            cur.next.prev = new_node
            cur.next = new_node
    return llist
