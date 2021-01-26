# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:2.__new__和__init__.py
@Time:NAME.py@Time:2021/1/25 20:36
"""
# __new__返回值：
# 1.返回为None,此时无法调用构造方法
# 2.返回为其他类实例，不会执行本类的构造方法
# 3.返回为该类实例，正常逻辑，能够正常走流程

class A():

    def __new__(cls, *args, **kwargs):
        print(1)
        return None

    def __init__(self):
        print(2)


a = A()     # 输出为1，因为__new__返回为空，因此无法创建实例对象，__init__不会被执行
print('*' * 20)


class B():
    def __new__(cls, *args, **kwargs):
        print(3)
        return super().__new__(cls)  # 调用基类的new返回该类的实例

    def __init__(self):
        print(4)


b = B()
# 输出为3，4；正常情况__new__就会返回该类的一个实例，因此走到了该构造方法
print('*' * 20)


class C():
    def __new__(cls, *args, **kwaargs):
        print(5)
        return b    # 返回其他类的实例，因此不会执行下方的构造方法

    def __init__(self):
        print(6)


c = C()
# 返回的为a，a的__new__返回为空，因此无法走到C的构造方法