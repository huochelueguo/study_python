# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:08_print函数.py
@Time:NAME.py@Time:2020/7/14 上午9:12
"""
# 这是print函数不换行方法：修改print函数中的缺省参数end的值
a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    print(a[i])  # 输出后，每一个值为一行

for i in range(len(a)):
    print(a[i], end=',')    # 修改end值，输出后在同一行，每个字用,分开
