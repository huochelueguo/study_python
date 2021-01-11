# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:05_practice.py
@Time:NAME.py@Time:2020/8/5 17:34
"""
# 装饰器练习
import time


def time_use(func):
    def wrapper(a, b):
        start = time.time()
        a = func(a, b)
        time.sleep(2)
        end = time.time()
        use = end - start
        print(f'执行函数耗时{use}')
        return a
    return wrapper


@time_use
def sum(a, b):
    # return a+b
    print(f'{a+b}')


print(sum(1, 2))

