# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:str_dict.py
@Time:NAME.py@Time:2020/8/3 下午11:40
"""
# 字符串转换为字典，使用eval,前提是该字符串长得比较像字典
str1 = "{'a': 1, 'b': 2}"
print(eval(str1))
print(type(eval(str1)))