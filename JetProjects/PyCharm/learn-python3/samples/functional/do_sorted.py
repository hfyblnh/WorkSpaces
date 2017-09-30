#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/9/30 18:15
# @Author  : Arteezy
# @Site    : 
# @File    : do_sorted.py
# @Software: PyCharm
from operator import itemgetter

print(sorted([36, 5, -12, 9, -21]))
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.upper, reverse=True))

# 用一组tuple表示学生名字和成绩
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88), ('Arteezy', 90)]
# 对上述列表分别按名字排序
print(sorted(L, key=itemgetter(0)))
# 再按成绩从高到低排序
print(sorted(L, key=itemgetter(1), reverse=True))
# 成绩从低到高排序
print(sorted(L, key=lambda t: t[1]))

# 小结
# sorted()也是一个高阶函数，用sorted()排序的关键在于实现一个映射函数
