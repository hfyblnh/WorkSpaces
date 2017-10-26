#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "bt3"

import collections
import sys


def count_unique_word_freq():
    return collections.Counter(sys.stdin.read().lower().split()).most_common()


if __name__ == '__main__':
    print(count_unique_word_freq())
