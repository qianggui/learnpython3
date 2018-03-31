#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import hashlib

## md5  128字节  32位的16进制字符串表示
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

##SHA1  160字节，40位的16进制字符串表示
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())