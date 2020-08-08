# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_迭代器生成.py
@Time:NAME.py@Time:2020/8/8 18:45
"""
# 创造迭代器的方法：iter()
list = [1, 2, 3, 4, 5]
it = iter(list)
print(type(it))     # <class 'list_iterator'>
