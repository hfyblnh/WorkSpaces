#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "bt3"

''' Implement a unordered linked list, i.e. a LIFO linked list (like a stack) '''

from node import Node


class LinkedListLIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def printList(self):
        node = self.head
        while node:
            print(node.value)
            node = node.pointer

    def delete(self, prev, node):
        self.length -= 1
        if not prev:
            self.head = node.pointer  # head后移一位
        else:
            prev.pointer = node.pointer

    def add(self, value):
        """在head增加"""
        self.length += 1
        self.head = Node(value, self.head)

    def find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    def find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    def deleteNode(self, index):
        node, prev, i = self.find(index)
        # if index == i:  # error!
        if index == i and node:
            self.delete(prev, node)
        else:
            print('Node with index {} not found'.format(index))

    def deleteNodeByValue(self, value):
        node, prev, found = self.find_by_value(value)
        if found:
            self.delete(prev, node)
        else:
            print('Node with value {} not found'.format(value))


if __name__ == '__main__':
    ll = LinkedListLIFO()
    for i in range(1, 5):
        ll.add(i)
    ll.deleteNode(4)
    print('The list is:')
    ll.printList()
    print('The list after deleting node with index 2:')
    ll.deleteNode(2)
    ll.printList()
    print('The list after deleting node with value 3:')
    ll.deleteNodeByValue(3)
    ll.printList()
    print('The list after adding node with value 15')
    ll.add(15)
    ll.printList()
    print("The list after deleting everything...")
    # for i in range(ll.length - 1, -1, -1):
    for i in range(7, -1, -1):
        ll.deleteNode(i)
    ll.printList()
