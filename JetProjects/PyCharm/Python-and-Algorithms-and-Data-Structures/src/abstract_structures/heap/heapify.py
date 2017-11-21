#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "bt3"

import math


class Heapify(object):
    def __init__(self, data=None):
        self.data = data or []
        for i in range(len(data) // 2, -1, -1):
            self.__max_heapify__(i)

    def __repr__(self):
        return '{}'.format(self.data)

    @staticmethod
    def parent(i):
        # return i >> 1  # 此处错误
        return math.ceil(i / 2) - 1

    @staticmethod
    def left_child(i):
        return (i << 1) + 1

    @staticmethod
    def right_child(i):
        return (i << 1) + 2  # +2 instead of +1 because it's 0-indexed.

    def __max_heapify__(self, i):
        left = self.left_child(i)  # 左子index
        right = self.right_child(i)  # 右子index
        n = len(self.data)
        largest = (left < n and self.data[left] > self.data[i]) and left or i  # 获取最大值的下标
        largest = (right < n and self.data[right] > self.data[largest]) and right or largest
        if i is not largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.__max_heapify__(largest)

    def extract_max(self):
        n = len(self.data)
        max_element = self.data[0]
        self.data[0] = self.data[n - 1]
        self.data = self.data[:n - 1]
        self.__max_heapify__(0)
        return max_element


def test_Heapify():
    l = [3, 2, 5, 1, 7, 8, 2]
    h = Heapify(l)
    print(h)
    assert (h.extract_max() == 8)


if __name__ == '__main__':
    test_Heapify()
