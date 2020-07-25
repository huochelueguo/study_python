# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:04_os模块2.py
@Time:NAME.py@Time:2020/7/22 下午11:20
"""
# 小练习：case文件名称和数据存放文件名称一致时，读取case测试数据
import os
import yaml


class Get_Data(object):
    # 通过传入地址，获取对应yaml中文件的封装类

    def __init__(self, file_name):
        self.path = '/Users/sunwenxiao/PycharmProjects/study_python/pythonstudy/28_内置函数和模块/'+file_name

    def get_yaml(self):
        with open(self.path, 'r') as f:
            list_data = yaml.load(f, Loader=yaml.FullLoader)    # 新版本yaml，转换python时必须带Loader参数
        return list_data


class Get_Path(object):
    # 将当前工作目录读取出来，获取文件名，去对应数据文件中读取数据封装类


    def get_path(self, file_path):
        path = os.path.split(file_path)[1]
        path_name = os.path.splitext(path)[0]
        # print(path)
        return path_name


if __name__ == '__main__':
    a = '/Users/sunwenxiao/PycharmProjects/study_python/pythonstudy/28_内置函数和模块/04_os模块2.py'
    print(f'文件名称是：{Get_Path().get_path(a)}')
    print(type(Get_Path().get_path(a)))
    file_name = Get_Path().get_path(a)
    Get_Data.get_yaml('04_os模块2')



