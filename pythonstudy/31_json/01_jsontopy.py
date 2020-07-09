# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_jsontopy.py
@Time:NAME.py@Time:2020/7/9 上午12:28
"""
# json.loads() — loads函数则是将json格式的数据解码，转换为Python字典;
# json内部数据需要使用双引号

import json

data_json = '{"a": "1", "b": "2", "c": 3}'
data_dict = json.loads(data_json)
print(data_json)

