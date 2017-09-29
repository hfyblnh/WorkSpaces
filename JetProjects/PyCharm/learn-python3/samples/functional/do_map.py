#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Lnh'

from collections import Iterator
from collections import Iterable

# 变量可以指向函数
print(abs(-10))
print(abs)
x1 = abs(-10)
f1 = abs
print(x1)
print(f1)


# 高阶函数Higher-order function
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
	return f(x) + f(y)


print(add(-6, 5, abs))


# 编写高阶函数，就是让函数的参数能够接收别的函数。
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。


# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f2(x):
	return x * x * x


r = map(f2, range(1, 11))
print(isinstance(range(1, 11), Iterator))
print(isinstance(range(1, 11), Iterable))
print(r)
# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(r))

print(list(map(str, range(1, 11))))
