#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from io import StringIO, BytesIO

f = StringIO('Hello!\nHi!\nGoodbye!');
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

g = BytesIO()
# g.write(b'\xe4\xb8\xad\xe6\x96\x87')
g.write('中文'.encode('utf-8'))
print(g.getvalue().decode('utf-8'))
print(g.read())

print('中文'.encode('utf-8'))