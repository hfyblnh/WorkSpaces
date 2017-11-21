#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "bt3"

import heapq


def merge_sorted_seq(seq1, seq2):
    """merge two sorted sequences with little overhead,
    the result will be sorted, which is different of doing just +"""
    result = []
    for c in heapq.merge(seq1, seq2):
        result.append(c)
    return result


def test_merge_sorted_seq():
    seq1 = [1, 2, 3, 8, 9, 10]
    seq2 = [2, 3, 4, 5, 6, 7, 9]
    seq3 = seq1 + seq2
    assert (merge_sorted_seq(seq1, seq2) == sorted(seq3))
    assert (merge_sorted_seq(seq1, seq2) == list(heapq.merge(seq1, seq2)))


if __name__ == '__main__':
    test_merge_sorted_seq()
