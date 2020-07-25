# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:04_os模块2.py
@Time:NAME.py@Time:2020/7/12 下午9:49
"""
# OS模块主要作用：对文件路径等进行操作
# 查看文件所在路径
import os
print(os.getcwd())

# 列出所在目录中文件内容
print(os.listdir())

# 分割文件路径和文件名称,使用os.path.split(路径)
file_path = os.getcwd()
print(os.path.split(file_path))

# 将目录和文件名合成一个路径
file_path = '/Users/sunwenxiao/PycharmProjects/study_python/pythonstudy'
file_name = '28_内置函数和模块'
file = os.path.join(file_path, file_name)
print(file)

# 将文件名称和后缀分隔开,使用os.path.splitext
file_path2 = '/Users/sunwenxiao/PycharmProjects/study_python/pythonstudy/28_内置函数和模块/04_os模块1.py'
file_list = os.path.splitext(file_path2)
print(file_list)



