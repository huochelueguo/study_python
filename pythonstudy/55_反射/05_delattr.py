# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:05_delattr.py
@Time:2021/7/28 9:38 上午
"""
"""
delattr：
    用来删除某个实例的属性，非实际删除，仅针对delattr中实例的属性删除了，其他实例还可以正常的进行调用
"""


class Demo:

    def __init__(self, num, age):
        self.num = num
        self.age = age

    def add(self):
        print('this is add method')
        return self.num + self.num

    def age1(self):
        print(f'age is {self.age}')
        return self.age


de = Demo(200, 0)
print(de.age1())
delattr(de, 'num')
# print(de.add())     # 因为上一句已经把num删除了，因此在此调用时会报错AttributeError: 'Demo' object has no attribute 'num'

de2 = Demo(100, 0)
print(de2.add())
