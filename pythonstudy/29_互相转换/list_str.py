# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:list_str.py
@Time:NAME.py@Time:2020/8/3 下午11:10
"""
# 列表转换为字符串
# 方法一：遍历后，输出内容
list1 = ['1a', 2, '3c', 4]
for i in list1:
    print(i, end=' ')
    # print(type(i))


# 使用 ''.join()方法,.前面的为连接每个序列值得连接符
# 这种方法要求列表中每个值都是str，不是int，否则无法输出
list2 = ['1', '2', '3', '4']
str1 = '_'.join(list2)
print(str1)
