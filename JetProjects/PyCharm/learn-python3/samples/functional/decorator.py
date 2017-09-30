#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/9/30 20:22
# @Author  : Arteezy
# @Site    : 
# @File    : decorator.py
# @Software: PyCharm
import functools


def now1():
	print("2017/9/30 20:22")


f1 = now1
print(f1())
print(now1.__name__)
print(f1.__name__)
'''
装饰器
现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
'''


def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)

	return wrapper


# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now2():
	print("2017/9/30 20:22")


f2 = now2
print(f2())
print(now2.__name__)
print(f2.__name__)
'''
调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)

由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
'''


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log2(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)

		return wrapper

	return decorator


@log2('execute')
def now3():
	print("2017/9/30 20:22")


f3 = now3
print(f3())
print(now3.__name__)
print(f3.__name__)


# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：now = log('execute')(now)

# 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'。
# 需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。


def log3(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)

	return wrapper


def log4(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)

		return wrapper

	return decorator


'''
小结
在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，
而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。
decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
'''
