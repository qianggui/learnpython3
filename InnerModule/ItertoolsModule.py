#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import itertools

##count 无限迭代器，打印自然数
natuals = itertools.count(1)

print('\n---------------华丽的分割线--------------\n')

##cycle 无限迭代器，循环打印ABC
cd = itertools.cycle('ABC')

## repeat 有限迭代器， 重复打印AB这整个字符串
ns = itertools.repeat('AB', 3)
for n in ns:
    print(n)

print('\n---------------华丽的分割线--------------\n')

ns1 = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns1))

print('\n---------------华丽的分割线--------------\n')

## chain 将一组迭代对象串联起来，形成一个更大的迭代
for c in  itertools.chain('ABC', 'XYZ'):
    print(c)

print('\n---------------华丽的分割线--------------\n')

## groupby 将迭代器中相邻的重复元素挑出来放一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

print('\n---------------华丽的分割线--------------\n')

for key, group in itertools.groupby('AaABbBCcAAA', lambda c: c.upper()):
    print(key, list(group))






