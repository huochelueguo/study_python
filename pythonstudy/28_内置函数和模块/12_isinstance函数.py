# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:12_isinstance函数.py
@Time:NAME.py@Time:2020/8/8 18:22
"""
# 函数作用：isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
# 和type的区别：有继承关系时，type仅读取子类类型，isinstance读取父类类型
# 使用方法：isinstance(object, classinfo)：对象和数据类型，返回bool
a = 1
print(isinstance(a, str))   # False
print(isinstance(a, int))   # True


class A(object):
    pass


class B(A):
    pass


print(isinstance(A, B))  # False
print(type(A) == type(B))   # True