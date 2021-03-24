# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:05_生成器加深理解.py
@Time:NAME.py@Time:2021/3/24 17:37
"""
from collections.abc import Iterable


def scq(start, end, step=1):
    print('begin')
    while start < end:
        yield start
        start += step


# 创建一个函数对象，因为函数中有yield关键字，因此不会调用函数，只是创建了一个函数的生成器
q = scq(1, 7, 2)

# 因为生成器也属于是迭代器，因此可以直接使用for循环输出所有内容，等同于注释内容
# print(next(q))
# print(next(q))
# print(next(q))
for i in q:
    print(i)

print(isinstance(q, Iterable))  # true