# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02.快速排序.py
@Time:2021/3/1 上午9:44
"""


def quicksort(testlist, start, end):
    if start > end:
        return testlist
    else:
        i, j = start, end
        base = testlist[i]
        while i < j:
            while i < j and (testlist[j] >= base):
                j -= 1
            testlist[i] = testlist[j]
            while i < j and (testlist[i] <= base):
                i += 1
            testlist[j] = testlist[i]
        testlist[i] = base
        quicksort(testlist, start, j-1)
        quicksort(testlist, j+1, end)
    return testlist


lists= [30,24,5,58,18,36,12,42,39,18]
print(quicksort(lists, 0, 9))
