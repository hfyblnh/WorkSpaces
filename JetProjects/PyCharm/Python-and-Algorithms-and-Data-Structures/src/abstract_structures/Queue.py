#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 5 min

__author__ = "bt3"


class Queue(object):
    def __init__(self):
        self.enq = []
        self.deq = []

    # 入列
    def enqueue(self, item):
        return self.enq.append(item)

    # 出列
    def dequeue(self):
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())  # 翻转list
        return self.deq.pop()

    def peak(self):
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
        if self.deq:
            return self.deq[-1]

    def size(self):
        return len(self.enq) + len(self.deq)

    def isEmpty(self):
        return not (self.enq + self.deq)


if __name__ == '__main__':
    q = Queue()
    for i in range(1, 11):
        q.enqueue(i)
    print('Size:', q.size())
    print('Is empty?', q.isEmpty())
    print('Peak: ', q.peak())
    print('Dequeuing...')
    for i in range(10):
        print(q.dequeue())
    print('Size:', q.size())
    print('Is empty?', q.isEmpty())
    print('Peak: ', q.peak())
