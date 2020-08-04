# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:list_dict.py
@Time:NAME.py@Time:2020/8/4 上午9:05
"""
# 列表转换为字典，可以先通过zip将两个列表组合为一个新的列表，在通过dict()方式转换为字典
# 注意：
# 1.zip组合成的数据类型为zip.需要使用list转换成列表,在使用dict转换为字典
# 2.这种转换仅支持2组列表，大于2组无法转换
li1 = [1, 2, 3, 4]
li2 = ['a', 'b', 'c', 'd']
# li3 = [5, 6, 7, 8]
zip = zip(li1, li2)
li3 = list(zip)
dic = dict(li3)
print(li3)
print(type(li3))
print(dic)
print(type(dic))

