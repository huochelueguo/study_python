# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:11.二分法查找数组.py
@Time:2021/4/21 上午9:22
"""
"""
使用二分法查找有序数组中是否存在某一个数字，返回该数组索引
"""
list1 = [-1, 3, 5, 6, 9, 111, 222, 555, 666]
num1 = 555


def find_num(li, num):
    middle = len(li) // 2
    if len(li) == 0:
        print('not in list')
        return
    if li[middle] == num:
        print(f'find it')
        return
    elif li[middle] > num:
        find_num(li[:middle], num)
    elif li[middle] < num:
        find_num(li[middle+1:], num)
    else:
        print('not in list')


find_num(li=list1, num=num1)