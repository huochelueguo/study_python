# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:Singeltonfromimport.py
@Time:NAME.py@Time:2021/1/26 18:02
"""

# 方法：创建一个类，并且创建一个类的实例，其他类引用该类时，仅引用类的实例

class Singel2(object):

    def __init__(self):
        pass


single2 = Singel2()
# print(single2)