#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "bt3"

"""implement a priority queue class"""

import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0  # 入列的顺序

    def push(self, item, priority):
        """优先级越高（即priority越大），-priority值越小"""
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


def test_PriorityQueue():
    """push and pop are all O(logN)"""
    q = PriorityQueue()
    q.push(Item('test1'), 1)
    q.push(Item('test2'), 4)
    q.push(Item('test3'), 3)
    q.push(Item('test4'), 7)
    q.push(Item('test5'), 2)
    q.push(Item('test6'), 5)
    q.push(Item('test7'), 9)
    assert (str(q.pop()) == "Item('test7')")
    assert (str(q.pop()) == "Item('test4')")
    assert (str(q.pop()) == "Item('test6')")
    assert (str(q.pop()) == "Item('test2')")
    assert (str(q.pop()) == "Item('test3')")
    assert (str(q.pop()) == "Item('test5')")
    assert (str(q.pop()) == "Item('test1')")


if __name__ == '__main__':
    test_PriorityQueue()
