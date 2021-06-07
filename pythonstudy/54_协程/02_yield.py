# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_yield.py
@Time:2021/5/21 上午9:16
"""
import time

"""
使用yeild也能够实现协程:
    当某一个函数遇到yield返回时，线程将终止该函数，执行其他函数，等到其他函数遇到yield暂时停止时，在返回到原函数继续执行，
    实现了单线程下的并发
"""


def practice1():
    while True:
        print('practice1 yield前')
        yield
        print('practice1 yield后')
        time.sleep(2)


def practice2():
    while True:
        print('practice2 yield前')
        yield
        print('practice2 yield后')
        time.sleep(3)


if __name__ == '__main__':
    p1 = practice1()
    p2 = practice2()
    while True:
        next(p1)
        next(p2)
# 执行p1遇到yield，开始执行p2，p2遇到yield再回来执行p1，循环往复

