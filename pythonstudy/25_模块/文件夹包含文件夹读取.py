# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:文件夹包含文件夹读取.py
@Time:NAME.py@Time:2020/7/24 上午8:46
"""
# 25_模块文件中，存在文件夹中还有文件夹的情况，通过嵌套的方法读取
import os


def get_file(path):
    for file in os.listdir(path):
        i = os.path.join(path, file)
        print(i)
        if os.path.isdir(i):    # 判断某个文件是否为文件夹时，最好使用os.path.join将路径和文件夹拼起来后再去判断
            print(f'路径中有文件夹包含文件夹的为：{file}')
            get_file(i)  # 如果路径为文件夹时，就使用递归计算，直到该路径为文件
        else:
            file_list.append(file)
            with open(i, 'r', encoding='utf-8')as readfile:
                read = readfile.read()
            with open('/Users/sunwenxiao/PycharmProjects/study_python/pythonstudy/25_模块/write0724', 'a+', encoding='utf-8') as writefile:
                writefile.write(read)


if __name__ == '__main__':
    path = '/Users/sunwenxiao/PycharmProjects/study_python/pythonstudy/25_模块'
    file_list = []
    get_file(path)
    print(file_list)




