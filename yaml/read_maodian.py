# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:read_maodian.py
@Time:NAME.py@Time:2020/8/6 17:46
"""
# 对带有锚点的yaml数据进行读取并且输出

import yaml

with open('file_maodian', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
