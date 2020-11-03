# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:04_匿名函数.py
@Time:NAME.py@Time:2020/8/7 18:10
"""

# 匿名函数不需要显示地定义函数名，使用【lambda + 参数 +表达式】的方式
# 写法：lambda [arg1 [,arg2, ... argN]] : expression
# 可以传入多个参数，但只能有一个表达式。
from functools import reduce

li1 = [2, 44, 65, 76, 100, 111]


def num(n, func):
    li2 = []
    for i in n:
        if func(i):     # func可以使用匿名函数代替
            li2.append(i)
    return li2


print(num(li1, lambda x: x % 2 == 0))
print(num(li1, lambda key: key * key > 100))


# map与lambda函数结合

li1 = ['TONY', 'PauL', 'tom']
l3 = list(map(lambda key: key[0].upper()+key[1:].lower(), li1))
print(l3)

# filter和lambda函数结合使用
# 输出100以内的奇数
li = []
for i in range(1,10):
    li.append(i)

l4 = list(filter(lambda x: x % 2 != 0, li))
print(l4)

# reduce和lambda函数结合使用,注意返回值为一个数，不是列表
l5 = reduce(lambda x, y: x * y, li)
print(f'0-10的阶乘为：{l5}')
