#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/2 15:09
# @File    : protected_student.py
# @Software: PyCharm
__author__ = 'Arteezy'


class Student(object):
	def __init__(self, name, score):
		self.__name = name  # 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
		self.__score = score

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')


SumaiL = Student('EG.SumaiL', 98)
# print(SumaiL.__name)
print(SumaiL.get_name())
print(SumaiL.get_score())
# SumaiL.set_score(125)

'''
有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。
'''
print('Do not use SumaiL._Student__name:', SumaiL._Student__name)
