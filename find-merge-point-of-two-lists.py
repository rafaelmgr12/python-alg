#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    # Write your code here
    if head1 is None or head2 is None:
        return -1
    else:
        temp1 = head1
        temp2 = head2
        while temp1 is not temp2:
            if temp1.next is None:
                temp1 = head2
            else:
                temp1 = temp1.next
            if temp2.next is None:
                temp2 = head1
            else:
                temp2 = temp2.next
        return temp1.data

