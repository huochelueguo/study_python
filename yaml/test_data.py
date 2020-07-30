# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_data.py
@Time:NAME.py@Time:2020/7/30 上午8:45
"""
import yaml

with open('test_data1', 'r', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.Loader)
    print(data)
    li = data['list']
    print(li)
    print(type(li))
