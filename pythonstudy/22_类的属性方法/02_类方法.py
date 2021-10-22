# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_类方法.py
@Time:NAME.py@Time:2021/1/27 18:39
"""
"""
类方法：
    定义：和类本身有关的方法，和实例无关
    创建：
        方法名上带装饰器@claseemethod
        方法括号中不是self，而是cls
    使用场景：
    
"""


class A(object):

    @classmethod
    def method1(cls):
        print('this is a 类方法')


a = A()
a.method1()  # 通过类的实例.可以调用类方法
A.method1()  # 通过类名可以直接调用类的方法
