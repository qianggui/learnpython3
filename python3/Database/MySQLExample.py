#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#导入mysql驱动
import mysql.connector

conn = mysql.connector.connect(user='root', password='12345678', database='test')
cursor = conn.cursor()
#创建表
cursor.execute('create table user (id VARCHAR(20) PRIMARY key, NAME VARCHAR (20))')
#插入一行记录，注意mysql的占位符是%s
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Micheal'])
cursor.rowcount
#提交事物
conn.commit()
cursor.close()
#运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', (1,))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

