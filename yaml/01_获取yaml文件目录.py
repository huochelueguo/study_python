# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_获取yaml文件目录.py
@Time:NAME.py@Time:2020/8/25 17:29
"""
# 获取测试case路径，通过替换文件夹名称和后缀名称，打开对应的yaml数据，返回
import os

a = __file__
print(type(a))
print('*' * 50)
b = a.replace('.py', '.yaml')
print(b)
print('*' * 50)
c = b.replace('yaml', 'data', 1)
print(c)
print('*' * 50)

e = os.getcwd()
print(os.path.split(e))
print('*' * 50)
print(os.path.splitext(a))
print('*' * 50)

