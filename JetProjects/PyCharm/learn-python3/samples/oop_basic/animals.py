#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/2 15:22
# @File    : animals.py
# @Software: PyCharm
__author__ = 'Arteezy'
' 继承和多态 '


# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。

class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()
cat = Cat()
cat.run()

# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(cat, Cat))
print(isinstance(cat, Animal))
print(isinstance(Animal(), Animal))
print(isinstance(Animal(), Dog))
print(isinstance(Animal(), Cat))


def run_twice(animal):
    animal.run()
    animal.run()


# 与C++一致，形参为指向基类的指针或者引用，实参为子类对象（实例）
run_twice(Animal())
run_twice(Cat())
run_twice(Dog())


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


run_twice(Tortoise())

'''
多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。
由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思。

对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法；
而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定；
这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。

这就是著名的“开闭”原则：
对扩展开放：允许新增Animal子类；
对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树。比如如下的继承树：

静态语言 vs 动态语言
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
'''


class Timer(object):
    def run(self):
        print('Start...')


'''
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。
许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
'''
run_twice(Timer())

'''
小结
继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
'''
