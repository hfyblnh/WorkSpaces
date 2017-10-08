#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable
from collections import Iterator

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for k in d:
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)

for ch in "2ez4rtz":
    print(ch)

print(isinstance('abc', Iterable))
print(isinstance(1234, Iterable))
print(isinstance([1, 2, 3, 4], Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Iterable and Iterator
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance((), Iterable))

print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance((), Iterator))

# 生成器都是Iterator对象
print(isinstance((x for x in range(1, 11)), Iterator))

# iter()函数把Iterable变成Iterator
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter(()), Iterator))

# 这是因为Python的Iterator对象表示的是一个数据流，
# Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# 小结
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的，例如：

for x in [1, 2, 3, 4, 5]:
    print(x)

# 实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
