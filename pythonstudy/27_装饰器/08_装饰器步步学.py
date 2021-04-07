# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:08_装饰器步步学.py
@Time:2021/3/31 上午9:13
"""

# 原函数
import time


def sum(a, b):
    time.sleep(3)
    return a*1000 + b
# print(sum(200000, 10))

# 需求：给该函数增加内容，展示运算该函数所需要时间

# 方法1：直接在函数内部添加
# 存在问题：修改了内部的代码
def sum(a, b):
    start= time.time()
    time.sleep(3)
    sum_num = a*1000 + b
    end = time.time()
    print(end-start)
    return sum_num
# print(sum(200000, 10))
# print('-' * 100)


# 方法2：在外部函数对象中增加时间计算
# 问题：如果有多个函数时，需要写多个时间计算
def sum(a, b):
    time.sleep(3)
    return a*1000 + b
#
# start = time.time()
# sum(200000, 10)
# end = time.time()
# print(end - start)
# print('-' * 100)


# 方法3：写一个函数，专门计算时间，中间传入sum()
# 注意：因为sum()需要传参，因此可以将参数给外部的函数，让其传入，使用*args, **kwargs
# 问题：wrapper中，调用的sum函数是写死的，没法复用
def wrapper(*args, **kwargs):
    start = time.time()
    sum_num = sum(*args, **kwargs)
    end = time.time()
    print(end - start)
    return sum_num
# print(wrapper(20000, 10))

# 方法4：使用func（）代替原函数
# 步骤：将warpper整体后退一格，新建一个outter()函数将其包起来，将sum替换为func，在outter中传入
def outter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        sum_num = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return sum_num
    return wrapper

@outter
def sum(a, b):
    time.sleep(3)
    return a*1000 + b
# print(wrapper(20000, 10))
print(sum(2000, 10))