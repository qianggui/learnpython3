#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import base64
after = base64.b64encode(b'binary\x00string')
print(after)
before = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(before)

print('\n---------------华丽的分割线--------------\n')

## url safe的base64编码
after2 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(after2)
before2 = base64.b64decode(b'abcd++//')
print(before2)
after3 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(after3)
before3 = base64.urlsafe_b64decode(b'abcd--__')
print(before3)


