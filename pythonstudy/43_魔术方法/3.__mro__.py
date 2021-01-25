# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:3.__mro__.py
@Time:NAME.py@Time:2021/1/25 21:19
"""

class a():

    def test(self):
        print(1)


class b(a):

    def test(self):
        print('enter b')
        super().test()
        print('leave b')


class c(a):

    def test(self):
        print('enter c')
        super().test()
        print('leave c')


class d(b, c):

    def test(self):
        print('enter d')
        super().test()
        print('leave d')


if __name__ == '__main__':
    print(d.__mro__)    # 多继承时，输出执行顺序
    dd = d()
    dd.test()