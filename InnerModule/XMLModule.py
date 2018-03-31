#!/usr/bin/env python3
# -*- coding:utf-8 -*-

## DOM SAX
from xml.parsers.expat import ParserCreate

class DefaultSaxhandler(object):
    def start_element(self, name, sttrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(sttrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax: char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li aline="center"><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxhandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)