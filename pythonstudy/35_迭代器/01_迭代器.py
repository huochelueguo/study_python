# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_迭代器.py
@Time:NAME.py@Time:2020/8/8 17:50
"""
# 迭代器概念：可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
"""
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的，例如：
"""
from collections.abc import Iterator
# 判断对象是否是迭代器，使用isinstance(对象, Iterator)
a = [1, 2, 3, 4]
print(isinstance(a, Iterator))  # False
