# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01.冒泡排序.py
@Time:2020/12/19 下午10:58
"""


def mppx(l1):
    list_len = len(l1)
    for i in range(list_len-1):
        print(l1[i])
        for j in range(list_len-i-1):
            print(l1[j], l1[j+1])
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
                print(l1)
    return l1


list_1 = [4, 3, 2]
print(mppx(list_1))
