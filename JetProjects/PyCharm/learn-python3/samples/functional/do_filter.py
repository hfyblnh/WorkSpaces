#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/9/30 13:11
# @Author  : Arteezy
# @Site    : 
# @File    : do_filter.py
# @Software: PyCharm

# Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。


def is_odd(n):
	return n % 2 == 1


print(list(filter(is_odd, range(1, 11))))


def not_empty(s):
	return s and s.strip()


print(list(filter(not_empty, ['abc', '', 'xyz', '', None, ''])))
