# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:07.带参数的装饰器2.py
@Time:NAME.py@Time:2020/11/5 18:55
"""
# 带参数的装饰器，且被装饰函数需要传入参数的情况


def zsq(flag):
    # 装饰器只能接收一个参数并且是函数类型
    def zhuangshiqi(func):
        def wrapper(a, b):
            # 根据参数判断执行内容
            if flag == '1':
                print('加fa')
                func(a, b)
            if flag == '2':
                print('减法')
                func(a, b)
        return wrapper
    # 此处需要多return
    return zhuangshiqi


@zsq(flag='1')
def add(a, b):
    print(f'a+b= {a+b}')


@zsq(flag='2')
def cheng(a, b):
    print(f'a * b = {a*b}')

add(1, 2)
cheng(2, 2)