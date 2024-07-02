# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_迭代器.py
@Time:NAME.py@Time:2020/8/8 17:50
"""
"""
迭代器：
可以被next()调用并且不断返回下一个值成为迭代器（Iterator），单纯重复的返回一个值不是迭代器【是一个对象】
    概念：指迭代取值的工具，迭代是重复的一个过程，每次都是基于上一个值得结果而继续，不是重复的返回一个值
    特征：
    1.可以基于next()迭代所有数据，一次取出一个值，节约空间
    2.只能往前进，不能够后退
    
可迭代对象：
可以使用for循环取值的对象都是可迭代对象(Iterable)
集合数据类型如list、dict、str等是Iterable但不是Iterator，可以通过iter()函数获得一个Iterator对象。

两者关系：
迭代器肯定是可迭代对象，但是可迭代对象不一定都是迭代器，比如list,str,dict等，只能通过iter()转换成迭代器

"""

from collections.abc import Iterator, Iterable
# 判断对象是否是迭代器，使用isinstance(对象, Iterator)
a = [1, 2, 3, 4]
b = iter(a)
print(isinstance(a, Iterator))  # False
print(isinstance(b, Iterator))


# 判断对象是否是可迭代对象，使用isinstance(对象, Iterable)
print(isinstance(a, Iterable))

for i in range(len(a)):
    print(f'迭代器每次输出的是:{next(b)}')
# 只有将列表等可迭代对象转换为迭代器才可以使用，否则报错
next(a) # TypeError: 'list' object is not an iterator