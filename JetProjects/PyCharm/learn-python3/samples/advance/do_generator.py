#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L1 = [x * x for x in range(1, 11)]
print(L1)

g1 = (x * x for x in range(1, 11))
print(g1)
for s in g1:
	print(s)


def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'


fib(9)


def fibg(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield (b)
		a, b = b, a + b
		n = n + 1
	return 'done'


f7 = fibg(7)
print(f7)
for f7data in f7:
	print(f7data)


def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield (3)
	print('step 3')
	yield (5)


o = odd()
print(next(o))
print(next(o))
print(next(o))

f8 = fibg(8)
while True:
	try:
		x = next(f8)
		print('f8:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break


def triangles():
	tri = [1]
	while True:
		yield tri
		tri = [sum(i) for i in zip([0] + tri, tri + [0])]


n = 0
for t in triangles():
	print(t)
	n = n + 1
	if n == 10:
		break
