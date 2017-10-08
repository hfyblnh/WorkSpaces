#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Lnh'
from functools import reduce


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def f1(x1, x2):
    return x1 + x2


print(reduce(f1, range(1, 7)))


def f2(x3, x4):
    return x3 * 10 + x4


print(reduce(f2, [1, 3, 5, 7, 9]))


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


# 配合map()，我们就可以写出把str转换为int的函数
print(reduce(f2, map(char2num, '147258')))
print(isinstance(reduce(f2, map(char2num, '147258')), int))


# 整理成一个str2int的函数就是：
def str2int1(s):
    def fn(x, y):
        return x * 10 + y

    def ch2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(ch2num, s))


def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
