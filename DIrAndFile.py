#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
name = os.name
print(name)
uname = os.uname()
print(uname)
environ = os.environ
print(environ)
abspath = os.path.abspath('.')
print(abspath)
t = os.path.split('/Users/playcrab/dev/python/learn/test.py')
print(t[0])
print(t[1])
t2 = os.path.splitext('/Users/playcrab/dev/python/learn/test.py')
print(t2[0])
print(t2[1])
