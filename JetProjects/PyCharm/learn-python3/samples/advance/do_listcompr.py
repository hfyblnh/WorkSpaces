#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print(list(range(5, 16)))
print([x * x for x in range(1, 11)])
print([m + n for m in 'abc' for n in 'XYZ'])

print([d for d in os.listdir('../../../../../')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, ':', v)

print([k + ':' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
