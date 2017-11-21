#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "bt3"

""" define a class for a set of stacks """

from stack import Stack


class SetOfStacks(Stack):
    def __init__(self, capacity=4):
        self.setofstacks = []
        self.content = []
        self.capacity = capacity

    def push(self, value):
        if self.size() >= self.capacity:
            self.setofstacks.append(self.content)
            self.content = []
        self.content.append(value)

    def pop(self):
        value = self.content.pop()
        if self.isEmpty() and self.setofstacks:
            self.content = self.setofstacks.pop()
        return value

    def sizeStack(self):
        return len(self.setofstacks) * self.capacity + self.size()

    def __repr__(self):
        aux = []
        for s in self.setofstacks:
            aux.extend(s)
        aux.extend(self.content)
        return '{}'.format(aux)


if __name__ == '__main__':
    capacity = 5
    stack = SetOfStacks(capacity)
    print("Is the stack empty? ", stack.isEmpty())
    print("Adding 0 to 10 in the stack...")
    for i in range(17):
        stack.push(i)
    print(stack)
    print("Stack size: ", stack.sizeStack())
    print("Stack peek: ", stack.peek())
    print("Pop...", stack.pop())
    print("Stack peek: ", stack.peek())
    print("Is the stack empty? ", stack.isEmpty())
    print(stack)
