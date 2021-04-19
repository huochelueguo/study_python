# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:12.有参装饰器实践.py
@Time:2021/4/15 下午11:36
"""

"""
需求：根据函数不同的参数，在装饰器中执行不同内容
思路：
    1。由于无法在装饰器外部函数中再添加新参数，因此需要在加一层，形成三层
    2。最外层函数新添加一个参数，普通函数书写语法糖时添加该参数，并且传入相对应的值
    3。第二层参数增加返回值return wrapper，讲原函数内容返回到公共区域
"""
import time


def yczsq(laiuyan):
    def timer(func):
        def wrapper(*args, **kwargs):
            if laiuyan =='excel':
                start = time.time()
                res = func(*args, **kwargs)
                time.sleep(1)
                print('excel睡眠1秒')
                end = time.time()
                print(end - start)
                return res
            if laiuyan == 'yaml':
                start = time.time()
                res = func(*args, **kwargs)
                time.sleep(2)
                print('yaml睡眠2秒')
                end = time.time()
                print(end - start)
                return res
            if laiuyan == 'mysql':
                start = time.time()
                res = func(*args, **kwargs)
                time.sleep(3)
                print('mysql睡眠3秒')
                end = time.time()
                print(end - start)
                return res
        return wrapper
    return timer


@yczsq(laiuyan='excel')
def excel(a, b):
    return a * b


@yczsq(laiuyan='yaml')
def yaml(a, b):
    return a - b


@yczsq(laiuyan='mysql')
def mysql(a, b):
    return a / b


print(excel(2, 2))
print(yaml(2, 2))
print(mysql(2, 2))