# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:08_菱形继承问题.py
@Time:NAME.py@Time:2021/3/25 14:51
"""
"""
题目：
已知A B C类（继承A类），D类（继承B类），E类（继承自CD），如果AD类都有demo()方法，调用E类的demo（）时，将会调用哪些类的demo（）
答案：
1.如果E类没有调用super，则只会调用E类自己的类
2.如果有调用super，则也会调用A类的demo
"""


class A():
    def demo(self):
        print('enter A')
        print('leave A')


class B():
    def __str__(self):
        print('B仅有初始化方法')


class C(A):
    def __str__(self):
        print('C仅有初始化方法')


class D(B):
    def demo(self):
        print('enter D')
        print('leave D')


class E(C, D):
    def demo(self):
        print('enter E')
        super().demo()
        print('leave E')


e = E()
e.demo()
print(E.__mro__)