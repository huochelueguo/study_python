# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@File:a_09读取文件名.py
@Time:2021/6/7 17:11
"""
"""
需求：读取指定文件夹下所有文件的名称，放入队列中
"""
import os
from queue import Queue
root_path = 'E:\python_study\pythonstudy'
q = Queue()
list1 =[]


def get_dirname(path):
    dir_list = os.listdir(path)
    # print(dir_list)
    for dir in dir_list:
        # 判断如果是文件夹，再次遍历该文件夹，直到全部为文件
        if os.path.isdir(os.path.join(path, dir)):
            # list1.append(dir)
            get_dirname(path=os.path.join(path, dir))
        elif os.path.isfile(os.path.join(path, dir)):
            q.put(dir)
            list1.append(dir)
    return q


qq = get_dirname(path=root_path)
print(qq.qsize())
print(qq.get())
print(len(list1), list1)

