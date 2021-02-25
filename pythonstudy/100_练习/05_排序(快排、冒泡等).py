# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:05_排序(快排、冒泡等).py
@Time:NAME.py@Time:2021/2/25 15:16
"""

"""
快速排序
    思路：1.在数列之中，选择一个元素作为”基准”（pivot），或者叫比较值。
        2.数列中所有元素都和这个基准值进行比较，如果比基准值小就移到基准值的左边，如果比基准值大就移到基准值的右边
        3.以基准值左右两边的子列作为新数列，不断重复第一步和第二步，直到所有子集只剩下一个元素为止
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



lists=[30,24,5,58,18,36,12,42,39]
print(quicksort(lists, 0, 8))
