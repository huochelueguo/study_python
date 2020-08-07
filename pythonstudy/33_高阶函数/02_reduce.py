# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_reduce.py
@Time:NAME.py@Time:2020/8/6 20:53
"""
# reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 注意：python3后，reduce()函数需要导入包后才可以使用
from functools import reduce

li1 = [1, 2, 3, 4, 5]


def add(a, b):
    return a + b


num = reduce(add, li1)
print(num)


# 练习：输出阶乘
li2 = []
for i in range(1, 101):
    li2.append(i)
print(li2)


def cheng(a, b):
    return a * b


sum2 = reduce(cheng, li2)
print(sum2)
