#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "bt3"

''' 
implement a function to see whether a linked list is circular. 
To implement this, we just need two pointers with different paces (for example, one goes twice faster)
'''

from linked_list_fifo import LinkedListFIFO
from node import Node


class CircularLinkedListFIFO(LinkedListFIFO):
    def add(self, value):
        self.length += 1
        node = Node(value, self.head)
        if self.tail:
            self.tail.pointer = node
        self.tail = node


def isCircularll(ll):
    p1 = ll.head
    p2 = ll.head

    while p2:
        try:
            p1 = p1.pointer
            p2 = p2.pointer.pointer
        except:
            break
        if p1 == p2:
            return True

    return False


if __name__ == '__main__':
    ll = LinkedListFIFO()
    for i in range(10):
        ll.addNode(i)
    ll.printList()
    print(isCircularll(ll))

    cirll = CircularLinkedListFIFO()
    for i in range(10):
        cirll.addNode(i)
    print(isCircularll(cirll))
