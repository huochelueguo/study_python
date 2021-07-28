# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:04_setattr.py
@Time:2021/7/26 9:22 上午
"""

"""
serattr的作用：
    为对象添加变量或方法,可以先判断该实例是否有某一个值或者方法，如果有的话再继续对值进行重新赋值操作
"""


class Demo:

    def __init__(self, num):
        self.num = num

    def add(self):
        print('this is add method')
        return self.num + self.num


de = Demo(200)
if hasattr(de, 'num'):
    setattr(de, 'num', 400)
    print(de.add())