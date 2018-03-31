#!/usr/bin/env python3
# -*-  coding:utf-8 -*-

import chardet

print(chardet.detect(b'Hello, world!'))

print('\n---------------华丽的分割线--------------\n')

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

print('\n---------------华丽的分割线--------------\n')

data2 = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data2))

print('\n---------------华丽的分割线--------------\n')

data3 = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data3))


