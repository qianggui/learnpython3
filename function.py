#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

def _not_divisable(n):
    return lambda x: x%n >0

def primes():
    yield 2
    it = _odd_iter() #初始序列
    while True:
        n = next(it) #返回序列第一个数
        yield n
        it = filter(_not_divisable(n), it) #构造新序列

for n in primes():
    if n < 1000:
        pass # print(n)
    else:
        break

x = filter(_not_divisable(3), [2,3,5,7,9]);
print(list(x))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return str.lower(t[0])
L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]
L3 = sorted(L, key=by_score, reverse=True)
print(L3)

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

def createCounter():
    s = [0]
    def counter():
        s[0]+=1
        return s[0]
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

def is_odd():
    # return n % 2 == 1
    return lambda x: x%2 == 1

L = list(filter(lambda x: x%2 == 1, range(1, 20)))
print(L)



