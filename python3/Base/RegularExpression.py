#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

result = re.match(r'^\d{3}\-\d{3,8}$', '010-123456789')
print(result)
result = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(result)
if re.match(r'^\d{3}\-\d{3,8}$', '010-123456789'):
    print('Yes')
else:
    print('No')

list1 = 'a b   c'.split(' ')
list2 = re.split(r'\s+', 'a b   c')
list3 = re.split(r'[\s\,\;]+', 'a,b,;; c  d')
print(list1)
print(list2)
print(list3)

m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.group(3))

# 编译正则表达式
re_telephone = re.compile(r'^(\d{3}-(\d{3,8}))')
group1 = re_telephone.match('010-12345')
group2 = re_telephone.match('010-12345678')
print(group1.group(2))
print(group2.group(2))

