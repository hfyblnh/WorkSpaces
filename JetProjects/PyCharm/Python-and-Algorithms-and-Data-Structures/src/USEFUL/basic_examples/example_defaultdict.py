#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "bt3"

from collections import defaultdict


def defaultdict_example():
    # show some examples for collections.defaultdict
    pairs = {('a', 1), ('b', 2), ('c', 3)}

    d1 = {}
    for key, value in pairs:
        if key not in d1:
            d1[key] = []
        d1[key].append(value)
    print(d1)

    d2 = defaultdict(list)
    for key, value in pairs:
        d2[key].append(value)
    print(d2)

    d3 = {}
    for key, value in pairs:
        d3.setdefault(key, []).append(value)
    print(d3)


if __name__ == '__main__':
    defaultdict_example()
