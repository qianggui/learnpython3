#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#name = input('please enter your name: ')
#print('hello,', name)
print(648*540+328*25+198*24+98*19+60*2+30*1+18*1+6*2)
print(648*28+328*30+198*12+98*60+60*4+30*6+18*1+6*4)
print(r'''hello
world''')

print(list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

n = 1
while n <= 100:
    if n >10:
        break
    print(n)
    n = n + 1
print('END' + str(n))

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

d = {'Micheal': 100, 'Bob': 75, 'Tracy': 85}
print(d['Micheal'])

s = set([1,2,3,4])
print(s)

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-666))

import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60 ,math.pi / 6)
print(str(x) + ' ' + str(y))
print(y)

def fact(n):
    if n == 1:
        return 1
    return n * fact(n -1 )
print(fact(3))



def fact2(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact2(5))

L = ['Micheal', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])

