# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:14_enumerate.py
@Time:NAME.py@Time:2021/1/20 18:42
"""
"""
作用：返回数组下标
写法：enumerate(可迭代数据, start=)
    start代表从X开始，默认为0
返回值：返回一个枚举，下标+数据组成的元组
    字典返回的为字典的key
"""
l1 = [11, 21, 31, 41, 51]
for i in enumerate(l1):
    print(i)

# 如果仅输出下标
for k, v in enumerate(l1, start=1):
    print(k)

dict1 = {'1': 'a', '2': 'b', '3': 'c'}
for k,v in enumerate(dict1):
    print(k,v)
for i in enumerate(dict1):
    print(i)
print(list(enumerate(dict1)))