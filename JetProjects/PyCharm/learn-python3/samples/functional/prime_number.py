#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/9/30 13:29
# @Author  : Arteezy
# @Site    : 
# @File    : prime_number.py
# @Software: PyCharm


def odd_iter():
	odd = 1
	while True:
		odd += 2
		yield odd


def _not_divisible(n):
	return lambda x: x % n > 0


def prime_number_iter():
	yield 2
	it = odd_iter()  # 初始序列，第一个数是3
	while True:
		first_num = next(it)  # 返回序列的第一个数
		yield first_num
		it = filter(_not_divisible(first_num), it)  # 构造新序列


# 打印1000以内的素数:
def main():
	for num in prime_number_iter():
		if num < 1000:
			print(num)
		else:
			break


if __name__ == '__main__':
	main()
