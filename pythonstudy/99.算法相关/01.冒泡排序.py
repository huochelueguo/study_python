# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01.冒泡排序.py
@Time:2020/12/19 下午10:58
"""


def mppx(testlist):
    long = len(testlist)
    for i in range(long-1):
        for j in range(long-i-1):
            if testlist[j] > testlist[j+1]:
                testlist[j],testlist[j+1] = testlist[j+1],testlist[j]
    return testlist



lists= [30,24,5,58,18,36,12,42,39,18]
print(mppx(lists))
