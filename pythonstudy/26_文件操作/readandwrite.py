# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:readandwrite.py
@Time:NAME.py@Time:2020/7/23 19:21
"""
import os
file_path = os.getcwd()
list_file = os.listdir()    # 读取当前文件夹所有文件
print(list_file)
for file_name in list_file:
    # file_name2 = str.split(file_name, '.')[0]
    with open(file_name, 'r', encoding='utf-8') as f:
        # 读取每个文件，返回为列表
        str = f.read()
        # print(f.read())
    with open('write0723', 'a', encoding='utf-8') as file:
        file.write(str)





