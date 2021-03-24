# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:07_生成器的应用.py
@Time:NAME.py@Time:2021/3/24 18:24
"""
"""
生成器实现斐波那契数列
"""


def fic():
    print(1)
    a = b = 1
    while True:
        yield b
        a, b = b, a+b   # b赋值给a，b


s = fic()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
for i in range(10):
    print(next(s))

