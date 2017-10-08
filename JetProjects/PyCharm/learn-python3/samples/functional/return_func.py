#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/9/30 18:42
# @Author  : Arteezy
# @Site    : 
# @File    : return_func.py
# @Software: PyCharm


def calc_sum1(*args):
    ax = 0
    for n in args:
        ax += n
    return ax


# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量。
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
def lazy_sum(*args):
    def calc_sum2():
        ax = 0
        for n in args:
            ax += n
        return ax

    return calc_sum2


print(calc_sum1(1, 3, 5, 7, 9))
print(lazy_sum(2, 4, 6, 8, 10))
print(lazy_sum(2, 4, 6, 8, 10)())


# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：

def count1():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


func1, func2, func3 = count1()
print(func1(), func2(), func3())

'''
在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
'''


# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count2():
    def f2(j):
        def g():
            return j * j

        return g

    fs2 = []
    for i in range(1, 4):
        fs2.append(f2(i))
    return fs2


func4, func5, func6 = count2()
print(func4(), func5(), func6())

'''
小结
一个函数可以返回一个计算结果，也可以返回一个函数。
返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
'''

'''
匿名函数
当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
'''
print(list(map(lambda x: x * x, range(1, 10))))
