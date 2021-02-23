# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:4__str__.py
@Time:2021/2/3 上午9:32
"""

"""
__str__魔术方法：
    作用：
        输出类的对象时，会将__str__方法中返回值输出，而不是默认内容
    注意点：
        该方法必须有返回值，并且为字符串
    调用方法：
        1.输出方法
        2.使用str()输出方法
"""


class A(object):

    def __init__(self):
        pass

    def __str__(self):
        return '调用lei的__str__方法'


a = A()
print(a)
print(str(a))

