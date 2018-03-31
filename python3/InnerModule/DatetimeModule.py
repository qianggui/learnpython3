#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import datetime, timedelta, timezone
##获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))
##获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
##datetime转为timestamp
print(dt.timestamp())

##timestamp转换为datetime
t = dt.timestamp()
print(datetime.fromtimestamp(t)) #本地时间
print(datetime.utcfromtimestamp(t)) #UTC时间

##str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
print(type(cday))

##datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

##datetime加减
now = datetime.now()
print(now)
now1 = now + timedelta(hours=10)
print(now1)
now2 = now - timedelta(days=1)
print(now2)
now3 = now +timedelta(days=2, hours=12)
print(now3)

##本地时间转为UTC时间
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8) #强制设置为UTC+8:00
print(dt)
print('--------------')
##时区转换
#拿到UTC时间，并强制设置时区为UTC+0.00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
#astimezone()将转换时区为北京时间：
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
#astimezone()将时区转换为京东时间：
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
#astimezone()将bj_dt转换时区为东京时间：
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
