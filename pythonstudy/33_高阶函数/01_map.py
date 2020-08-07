# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_map.py
@Time:NAME.py@Time:2020/8/6 18:49
"""

# map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
# 使用方法：  map（函数名[无括号]，列表名）
# 注意：Python3版本之后，map返回值为一个迭代器，需要强转成list
List = [1, 2, 3, 4, 5, 6, 7]


def func(x):
    return x * x


data = map(func, List)
print(list(data))
print(map(func, List))

# 练习，将列表中的不规范名称按照首字母大写，其余小写输出
# 注意返回的结果只能迭代一次，如果需要多次使用请提前保存结果并处理
li1 = ['TONY', 'PauL', 'tom']


def letter(s):
    print(s, type(s))
    str = s[0].upper()+s[1:].lower()  # 使用字符串切片，改变每个数据的大小写
    return str


li2 = map(letter, li1)
print(list(li2))    # ['Tony', 'Paul', 'Tom']
print(list(li2))    # [] 由于迭代器只能迭代一次，因此在此输出时为空


