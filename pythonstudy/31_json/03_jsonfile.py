# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03_jsonfile.py
@Time:NAME.py@Time:2020/7/9 上午9:00
"""
# 对于json文件类型处理，则使用json.load()和json.dump()

import json


dict1 = {'name': '张三', 'age': 10, 'height': 180, 'sport': 'bike'}
with open('data. txt', 'a', encoding='utf-8') as f:
    # f.write(json.dumps(dict1, indent=4, ensure_ascii=False))
    # 必要参数：传入数据源、输出数据源、空格、避免中文编码异常
    json.dump(dict1, f, indent=4, ensure_ascii=False)
with open('data. txt', 'r', encoding='utf-8') as f:
    dict2 = json.load(f)
    print(dict2)

