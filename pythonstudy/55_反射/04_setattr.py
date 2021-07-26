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
    为对象添加变量或方法
"""


class Demo:

    def __init__(self, num):
        self.num = num

    def add(self):
        print('this is add method')
        return self.num + self.num