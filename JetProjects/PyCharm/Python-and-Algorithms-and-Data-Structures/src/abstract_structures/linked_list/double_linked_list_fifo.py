#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "bt3"

'''
Implement a double-linked list, which is very simple, we just need inherits
from a LinkedList Class and add an attribute for previous.
'''

from linked_list_fifo import LinkedListFIFO


class dNode(object):
    def __init__(self, value=None, pointer=None, previous=None):
        self.value = value
        self.pointer = pointer
        self.previous = previous


class dLinkList(LinkedListFIFO):
    def printListInverse(self):
        node = self.tail
        while node:
            print(node.value)
            try:
                node = node.previous
            except:
                break

    def add(self, value):
        self.length += 1
        node = dNode(value)
        if self.tail:
            self.tail.pointer = node
            node.previous = self.tail
        self.tail = node

    def delete(self, node):
        self.length -= 1
        node.previous.pointer = node.pointer
        if not node.pointer:
            self.tail = node.previous

    def find(self, index):
        node = self.head
        i = 0
        while node and i < index:
            node = node.pointer
            i += 1
        return node, i

    # delete nodes in general
    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            self.deleteFirst()
        else:
            node, i = self.find(index)
            if i == index and node:
                self.delete(node)
            else:
                print('Node with index {} not found'.format(index))


if __name__ == '__main__':
    dll = dLinkList()
    for i in range(1, 5):
        dll.addNode(i)
    dll.deleteNode(4)
    print('Printing the list...')
    dll.printList()
    print('Now, printing the list inversely...')
    dll.printListInverse()
    print('The list after adding node with value 15')
    dll.add(15)
    dll.printList()
    print("The list after deleting everything...")
    # for i in range(dll.length - 1, -1, -1):
    for i in range(7, -1, -1):
        dll.deleteNode(i)
    dll.printList()
