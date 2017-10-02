#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/2 15:58
# @File    : type_attr.py
# @Software: PyCharm
import types

__author__ = 'Arteezy'
' 获取对象信息 '

print(type(123))
print(type('str'))
print(type(None))

print(type(abs))

print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))


def fn():
	pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# do not compare types, use 'isinstance()'
print('do not compare types, use \'isinstance()\'')
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))
print(isinstance(fn, types.FunctionType))
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
print(len('ABC'))
print('ABC'.__len__())


# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法
class MyDog(object):
	def __len__(self):
		return 100


dog = MyDog()
print(len(dog))


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
	def __init__(self):
		self.x = 9

	def power(self):
		return self.x * self.x


print('attr')
obj = MyObject();
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 21)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(getattr(obj, 'z'))

'''
小结
通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
'''


# 一个正确的用法的例子如下：
def readImage(fp):
	if hasattr(fp, 'read'):
		return readData(fp)
	return None
