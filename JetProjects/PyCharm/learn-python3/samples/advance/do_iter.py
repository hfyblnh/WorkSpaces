#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable

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
