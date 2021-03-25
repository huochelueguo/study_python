# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:08_多重继承问题（非菱形继承）.py
@Time:NAME.py@Time:2021/3/25 16:30
"""

"""
非菱形继承时，继承顺序：
    则会按照先找B这一条分支，然后再找C这一条分支，最后找D这一条分支的顺序直到找到我们想要的属性
注意：
1.找到后就不会继续再执行啦！
2.只有调用了父类才会逐级查找
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

    # # C类有demo，因此不会在向上找父类A，如果没有再去父类A
    # def demo(self):
    #     print('enter C')
    #     print('leave C')


class D(B):
    def demo(self):
        print('enter D')
        print('leave D')


class E(C, D):
    def demo(self):
        print('enter E')
        super().demo()
        # 如果在调用一次super，也是从C类开始查找
        # super().demo()
        print('leave E')


e = E()
e.demo()
print(E.__mro__)
# 输出：enter E
# enter A
# leave A
# leave E
# (<class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.D'>, <class '__main__.B'>, <class 'object'>)