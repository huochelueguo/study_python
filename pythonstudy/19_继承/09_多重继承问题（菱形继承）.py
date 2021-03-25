# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:09_多重继承问题（菱形继承）.py
@Time:NAME.py@Time:2021/3/25 16:39
"""
"""
当继承关系为菱形继承时，继承顺序为（A同时继承于B C，BC同时继承于D）：
    经典类：一条路走到黑，深度优先【python2.X】
        土话：A先去找B，B没有去找D，如果没有A再去找C-D
    新式类：不找多各类最后继承的同一个类，直接去找下一个父类，广度优先【python3.x】
        土话，A先去找B，B没有时，再去看C，通过C找D
"""


class A():

    def demo(self):
        print('enter A')
        print('leave A')


class B(A):

    def demo(self):
        print('enter B')
        super().demo()
        print('leave B')


class C(A):

    def demo2(self):
        print('enter C')
        super().demo()
        print('leave C')


class D(C, B):

    def demo(self):
        print('enter D')
        super().demo()
        print('leave D')


# 在python3.x中，都是新式类，因此执行广度优先，在父类C中没有找到demo方法，就去父类B中找demo，B中找到了，但是B还有对其父类引用，因此还要先去
# 其父类A中执行demo，因此执行顺序为D--C(BREAK)--B--A--B--D
# 输出：enter D
# enter B
# enter A
# leave A
# leave B
# leave D
# (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
d = D()
d.demo()
print(D.__mro__)


