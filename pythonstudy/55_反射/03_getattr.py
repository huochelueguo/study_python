# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03_getattr.py
@Time:2021/7/26 9:16 上午
"""

"""
getattr的作用：
    用来获取对象中的方法或内存地址,一共三个参数：对象，名称，未找到时的返回值（如果设置了返回值，未找到时不会报错，否则会报错）
"""


class Demo:

    def __init__(self, num):
        self.num = num

    def add(self):
        print('this is add method')
        return self.num + self.num


de = Demo(233)
print(getattr(de, 'num'))  # 获取实例的属性：233
print(getattr(de, 'add'))  # 获取实例方法的内存地址：<bound method Demo.add of <__main__.Demo object at 0x10947d220>>
print(getattr(de, 'add1', 'not found'))  # 由于设置了返回值，因此未报错
print(getattr(de, 'add1'))  # 报错：AttributeError: 'Demo' object has no attribute 'add1'
