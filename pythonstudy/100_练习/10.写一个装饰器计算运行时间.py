# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:10.写一个装饰器计算运行时间.py
@Time:NAME.py@Time:2021/4/9 20:55
"""
"""
写一个计算并打印函数运行时间的装饰器，输出函数名称，函数参数，以及函数运行时间
"""
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(2)
        res = func(*args, **kwargs)
        end = time.time()
        print(f'函数运行时间为{end-start}')
        # print(func)
        return res
    return wrapper


@timer
def sum(a, b):
    print(f'函数名称是：{sum.__name__}')  # 输出函数名称 xx.__name__
    return a*b
print(sum(5, 5))
print('*' * 100)

"""
上下两种方法实现一样，只是一个使用了语法糖，一个使用的闭包的写法
闭包写法：将sum函数作为参数传给timer，将timer(sum)赋值给index。相当于获取了sum函数的内存地址，之后index(x,y)等同于执行sum(x,y)
"""


def sum2(a, b):
    print(f'函数名称是：{sum.__name__}')  # 输出函数名称 xx.__name__
    return a*b
index = timer(sum2)
print(index(6, 6))