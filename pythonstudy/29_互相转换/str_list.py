# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:str_list.py
@Time:NAME.py@Time:2020/8/3 20:45
"""
# str转换为list：使用str的切片方法，返回为列表
str1 = '你好'
print(str1.split())
str2 = 'hello python, go, go, go, go, go'
# 默认根据空格进行分割，分割成列表元素
print(str2.split())
# 可以指定根据某个字段进行分割，默认为第一个参数
print(str2.split(','))
# 2是最多将字符串分割的长度
print(str2.split(',', 2))
# 获取转换后列表中的第N位值
print(str2.split(',', 2)[0])
