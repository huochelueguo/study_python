# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:05_字符串练习.py
@Time:2021/1/20 上午9:28
"""
# l1 = ['s', 'u', 'p', 'e', 'r']，输出为super
# 方法1：
l1 = ['s', 'u', 'p', 'e', 'r']
str1 = ''
for i in l1:
    str1 += i
print(str1)
# 方法2：
s = ''
for i in l1:
    s += ''.join(i)
print(s)