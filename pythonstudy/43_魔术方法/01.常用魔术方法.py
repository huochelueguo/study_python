# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01.常用魔术方法.py
@Time:2021/1/22 上午9:26
"""
class NewAdd():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        # 未修改过的__str__输出为：<__main__.NewAdd object at 0x107ed0df0>
        # 修改过后为返回语句，注意返回必须为字符串
        return '这是修改过的类描述'


c = NewAdd(2, 2)
print(c)




