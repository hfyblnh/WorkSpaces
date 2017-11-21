#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "bt3"

""" Implement the 'towers of hanoi' """

from linked_stack import Stack


def moveTop(s1, s3):
    # s3.append(s1.pop())
    s3.push(s1.pop())


def moveDisks(n, s1, s3, s2):
    if n < 1: return
    moveDisks(n - 1, s1, s2, s3)
    moveTop(s1, s3)
    moveDisks(n - 1, s2, s3, s1)


def towersOfHanoi(n):
    # s1 = [x + 1 for x in range(n)]
    # s2 = []
    # s3 = []
    # print('The first stick is {0} and the third stick has {1}'.format(s1.printList(), s3.printList()))
    # print('The first stick is {0} and the third stick has {1}'.format(s1.printList(), s3.printList()))

    s1 = Stack()
    for x in range(n):
        s1.push(n - x)
    s2 = Stack()
    s3 = Stack()

    print('before move s1:')
    s1.printList()
    print('before move s3:')
    s3.printList()

    moveDisks(n, s1, s3, s2)

    print('after move s1:')
    s1.printList()
    print('after move s3:')
    s3.printList()

    return s3


if __name__ == '__main__':
    towersOfHanoi(6)
