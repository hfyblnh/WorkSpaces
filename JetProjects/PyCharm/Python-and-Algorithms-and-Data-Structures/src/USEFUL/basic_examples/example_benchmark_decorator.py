#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "bt3"

import random


# 基准，标准检查程序
def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print("%s" % func.__name__, time.clock() - t)
        return res

    return wrapper


@benchmark
def random_tree(n):
    temp = [n for n in range(n)]
    for i in range(n + 1):
        temp[random.choice(temp)] = random.choice(temp)
    return temp


if __name__ == '__main__':
    random_tree(10000)
