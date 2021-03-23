# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:07_查找匹配文件名路径.py
@Time:NAME.py@Time:2021/3/23 17:26
"""
"""
题目：
    编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出绝对/相对路径
思路：
    判断当前是否是文件，不是的话，递归查找到文件，在进行对比
"""
import os


def search_file(name, path):

    for file in os.listdir(path):
        file_real_path = os.path.join(path+'/'+file)
        if os.path.isfile(file_real_path):
            if name in file:
                print(file_real_path)
                print(os.path.split(file_real_path)[-1])
                print('-' * 20)
        else:
            # print(file_real_path)
            search_file(name, file_real_path)


if __name__ == "__main__":
    search_file("0", 'E:/Program Files (x86)/360Chrome/Chrome/Application')
