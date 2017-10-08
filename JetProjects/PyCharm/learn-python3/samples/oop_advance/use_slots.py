#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/5 16:57
# @File    : use_slots.py
# @Software: PyCharm
from types import MethodType

' __slots__ '
__author__ = 'Arteezy'


class Student(object):
    pass


# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
s = Student()
s.name = 'EG.SumaiL'  # 动态给实例绑定一个属性
print(s.name)


def set_age(self, age):  # 定义一个函数
    self.age = age


set_age = MethodType(set_age, s)  # 给实例绑定一个方法
set_age(25)
print(s.age)


def set_score(self, score):
    self.score = score


# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
Student.set_score = set_score


# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class StudentSlots(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s_slot = StudentSlots()
s_slot.name = 'EG.Fear_'
s_slot.age = '30'
# s_slot.score = '90'  # AttributeError: 'StudentSlots' object has no attribute 'score'

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
