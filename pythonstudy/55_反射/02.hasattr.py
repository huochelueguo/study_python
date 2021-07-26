# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02.hasattr.py
@Time:2021/7/26 9:07 上午
"""
"""
hasattr作用：
    在不知道函数有哪些方法的情况下，可以使用hasattr来判断，如果为真在继续进行
"""


class Demo:

    def __init__(self, num):
        self.num = num

    def add(self):
        print('this is add method')
        return self.num + self.num


de = Demo(666)
if hasattr(de, 'add1'):     # 判断是否有该方法
    print('class has this method')
    print(de.add())
else:
    print('error')