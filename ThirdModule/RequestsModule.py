#!/usr/bin/env python3
# -*-  coding:utf-8 -*-

import requests
r = requests.get('https://www.douban.com')
print(r.status_code)
print(r.headers)
print(r.headers['Content-Type'])
##获取cookie
print(r.cookies)
#print(r.cookies['ts'])
#print(r.text)

print('\n---------------华丽的分割线--------------\n')

r2 = requests.get('https://www.douban.com/search', params={'q':'python', 'cat':'100'})
##实际请求的URL
print(r2.url)
##查看编码
print(r2.encoding)
##获取bytes对象
print(r.content)

print('\n---------------华丽的分割线--------------\n')

##json
r3 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r3.json())

print('\n---------------华丽的分割线--------------\n')

##传入HTTP Header
r4 = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
#print(r4.text)

print('\n---------------华丽的分割线--------------\n')

##POST请求
r5 = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

##POST json
#params = {'key': 'value'}
#r6 = requests.post(url, json=params) ##内部自动序列化为JSON

##上传文件
#upload_files = {'file': open('report.xls', 'rb')}
#r7 = requests.post(url, files = upload_files)

##传入Cookie
#cs = {'token' : '123456', 'status' : 'working'}
#r8 = requests.get(url, cookies = cs)

##指定超时
#r9 = requests.get(url, timeout=2.5) #2.5秒后超时
