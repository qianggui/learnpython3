#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()

print('\n---------------华丽的分割线--------------\n')

## @contextmanager

from contextlib import contextmanager

class Query2(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query2(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()

print('\n---------------华丽的分割线--------------\n')

## 代码前后插入内容

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag('h1'):
    print("hello")
    print("world")

print('\n---------------华丽的分割线--------------\n')

## @closing

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


print('\n---------------华丽的分割线--------------\n')

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()