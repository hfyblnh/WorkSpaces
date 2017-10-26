#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "bt3"

from collections import Counter


# 回文构词法：变换或颠倒字母顺序而成另一词的
def is_anagram(s1, s2):
    """
    >>> is_anagram('cat', 'tac')
    True
    >>> is_anagram('cat', 'hat')
    False
    >>> is_anagram('Arteezy', 'rtzAeey')
    True
    >>> is_anagram('回文构词法', '构词法回文')
    True
    """
    counter = Counter()
    for c in s1:
        counter[c] += 1

    for c in s2:
        counter[c] -= 1

    for i in counter.values():
        if i:
            return False

    return True


# verify if words are anagrams by comparing a sum of  Unicode code point of the character
def get_unicode_sum(word):
    s = 0
    for p in word:
        s += ord(p)
    return s


def is_anagram2(word1, word2):
    """
    >>> is_anagram2('cat', 'tac')
    True
    >>> is_anagram2('cat', 'hat')
    False
    >>> is_anagram2('回文构词法', '构词法回文')
    True
    """
    return get_unicode_sum(word1) == get_unicode_sum(word2)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
