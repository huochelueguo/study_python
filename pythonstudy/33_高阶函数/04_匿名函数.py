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
li1 = [2, 44, 65, 76, 100, 111]


def num(n, func):
    li2 = []
    for i in n:
        if func(i):     # func可以使用匿名函数代替
            li2.append(i)
    return li2


print(num(li1, lambda x: x % 2 == 0))
print(num(li1, lambda key: key * key > 100))

# 传入多个参数
l3 = [12, 4, 5, 36, 10, 111]


def sum2(a, b):
    l4 = []
    for i in range(len(a)):
        c = a[i] * b[i]
        l4.append(c)
    return l4

print(sum2(li1, l3))



