#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#导入
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类
Base = declarative_base()

#定义User对象
class User(Base):
    #表的名字
    __tablename__ = 'user'

    #表的结构 需要加上primary_key 不然会报错
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

#初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:12345678@localhost:3306/test')
#创建DBSession类型
DBSession = sessionmaker(bind=engine)

#创建session对象
session = DBSession()
#创建新User对象
new_user = User(id='2', name='Jim')
#添加session
#session.add(new_user)
#提交即保存到数据库
#session.commit()
#关闭session
session.close()


##查询
#创建Session
session = DBSession()
#创建Query查询，filter是where条件，最后调用one()
#返回唯一行，如果all()则返回所有行
#user = session.query(User).filter(User.id=='1').one()
user = session.query(User).all()
#打印类型和对象的name属性
print('type:', type(user))
print(user)
for u in user:
    print(u.id , '-----' , u.name)
#print('name:', user.name)
#关闭session
session.close()
