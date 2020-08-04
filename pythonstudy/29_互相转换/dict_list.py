# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:dict_list.py
@Time:NAME.py@Time:2020/8/4 上午9:25
"""
# 字典转换为列表，直接使用dict的key或者value方法，直接取出值转换为列表
dict1 = {"name": "zhangsan", "age": 18, "sing_dog": False}
li1 = list(dict1.keys())
li2 = list(dict1.values())
print(li1, li2)
print(type(li1))
print(type(li2))
