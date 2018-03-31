#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import namedtuple

##namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))
Circle = namedtuple('Circle', ['x', 'y', 'r'])
circle = Circle(1,2,3)
print(circle.x)
print(circle.y)
print(circle.r)

print('\n---------------华丽的分割线--------------\n')

##deque 双向链表
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

print('\n---------------华丽的分割线--------------\n')

##defaultdict key不存在时，返回默认值
from collections import defaultdict
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

print('\n---------------华丽的分割线--------------\n')

##OrderedDict 按照key的插入顺序排序
from collections import OrderedDict
d = dict([('a', 1),('c', 2),('b', 3)])
print(d)
od = OrderedDict([('a', 1),('b', 2),('c', 3)])
print(od)

print('\n---------------华丽的分割线--------------\n')

## OrderDict 实现FIFO先进先出的dict
class LastUpdateOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

fifoDict = LastUpdateOrderedDict(3)
#fifoDict = OrderedDict()
fifoDict['a'] = 'A'
fifoDict['b'] = 'B'
fifoDict['c'] = 'C'
fifoDict['a'] = 'D'
print(fifoDict)

print('\n---------------华丽的分割线--------------\n')

## Counter
from collections import Counter
c = Counter()
for ch in 'programimg':
    c[ch] = c[ch] + 1
print(c)