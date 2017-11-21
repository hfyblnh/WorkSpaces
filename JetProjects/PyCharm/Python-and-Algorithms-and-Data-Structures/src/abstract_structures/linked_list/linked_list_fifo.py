#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "bt3"

''' A class for a linked list that has the nodes in a FIFO order (such as a queue) '''

from node import Node


class LinkedListFIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None  # this is different from ll lifo

    def printList(self):
        node = self.head
        while node:
            print(node.value)
            node = node.pointer

    def addFirst(self, value):
        self.length = 1
        node = Node(value)
        self.head = node
        self.tail = node

    def deleteFirst(self):
        self.length = 0
        self.head = None
        self.tail = None
        print('The list is empty.')

    def add(self, value):
        self.length += 1
        node = Node(value)
        if self.tail:
            self.tail.pointer = node
        self.tail = node

    def addNode(self, value):
        if not self.head:
            self.addFirst(value)
        else:
            self.add(value)

    def find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            self.deleteFirst()
        else:
            node, prev, i = self.find(index)
            if i == index and node:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer  # head后移一位
                else:
                    prev.pointer = node.pointer
                # if not self.tail == node:  # error!
                if self.tail == node:
                    self.tail = prev
            else:
                print('Node with index {} not found'.format(index))


if __name__ == '__main__':
    ll = LinkedListFIFO()
    for i in range(1, 5):
        ll.addNode(i)
    print('The list is:')
    ll.printList()
    print('\nThe list after deleting node with index 2:')
    ll.deleteNode(2)
    ll.printList()
    print('\nThe list after adding node with value 15')
    ll.add(15)
    ll.printList()
    print("\nThe list after deleting everything...")
    for i in range(ll.length - 1, -1, -1):
        ll.deleteNode(i)
    ll.printList()
