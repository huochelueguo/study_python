# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:06_format函数.py
@Time:NAME.py@Time:2020/7/13 下午10:12
"""
# format函数主要是用来构造字符串，
# 基本语法是通过  {} 符号操作，并且每一个 {} 都可以设置顺序，分别与format的参数顺序对应，
# 如果没有设置{}下标，默认重0开始递增
str1 = "{}{}{}{}".format(5, 7, 9, 10)
print(str1)

try:
    str2 = '{5}{4}{3}{2}{1}{0}'.format(1, 2, 3, 4, 5, 6)
except Exception as result:
    print(result)
else:
    print(str2)

