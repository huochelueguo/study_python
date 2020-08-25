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
print('*' * 50)

# 列出所在目录中文件内容
print(os.listdir())
print('*' * 50)
# 分割文件路径和文件名称,使用os.path.split(路径)
file_path = os.getcwd()
print(os.path.split(file_path))
print('*' * 50)
# 将目录和文件名合成一个路径
file_path = '/Users/sunwenxiao/PycharmProjects/study_python/pythonstudy'
file_name = '28_内置函数和模块'
file = os.path.join(file_path, file_name)
print(file)
print('*' * 50)
# 获取当前文件名称，去掉后缀方法1,使用os.path.splitext取出非后缀路径，在通过字符串分割取出
file_path2 = '/Users/sunwenxiao/PycharmProjects/study_python/pythonstudy/28_内置函数和模块/04_os模块1.py'
file_list = os.path.splitext(file_path2)
file2 = file_list[0]
file3 = file2.split('/')[-1]
print(file3)
print('*' * 50)
# 获取当前文件名称，去掉后缀方法2，先使用分割文件名路径方法分开后，使用字符串的split方法进行切割
list_os = os.path.split(__file__)
print(list_os[-1].split('.')[0])
print('*' * 50)
# 获取当前文件名称，去掉后缀方法3，直接使用__file__获取当前文件路径，使用两次split对路径进行切割，获取返回值
file_pa = __file__
print((file_pa.split('.')[-2]).split('/')[-1])
print('*' * 50)
# 读取当前路径可以直接使用__file__
print(__file__)
print('*' * 50)
