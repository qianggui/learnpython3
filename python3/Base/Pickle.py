#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pickle
import json

d = dict(name = 'Bob', age = 20, score = 88)
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
nd = pickle.load(f)
f.close()
print(nd)
print(nd['name'])

print('----------------------')
d1 = dict(name = 'Bob', age = 20, score = 88)
dstr = json.dumps(d1)
print(d1)
print(d1.get('age'))
print(dstr)
print('----------------------')
djson = json.loads(dstr)
print(djson['name'])