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


def all_time(func):
    def warpper():
        start = time.time()
        func()
        end = time.time()
        ti = end-start
        print(f'耗时为:{ti}')
    return warpper  # 此处返回值不要带（），否则就执行了


@all_time
def cal():
    for i in range(100000000):
        pass


cal()
