# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_对称数组问题.py
@Time:NAME.py@Time:2021/1/28 18:09
"""

"""
要求：判断数组元素是否对称。例如[1，2，0，2，1]，[1，2，3，3，2，1]这样的都是对称数组
用Python代码判断，是对称数组打印True，不是打印False,如：
x = [1, "a",  0, "2", 0, "a", 1]
"""

# 方法1，通过列表翻转判断是否是一个


def method_one(list):
    list2 = list[::-1]
    return list == list2


a = [2, 3, 4, 5]
b = [3, 4, 5, 4, 3]
c = ['3', 4, 4, '3']
print(method_one(a))
print(method_one(b))
print(method_one(c))
print('*' * 50)
# 方法2，通过比较


def method_two(list):
    len_list = len(list)
    for i in range(int(len_list/2)):
        if list[i] != list[-i-1]:
            return False
    return True


d = [2, 3, 4, 5]
e = [3, 4, 5, 4, 3]
f = ['3', 4, 4, '3']
print(method_one(a))
print(method_one(b))
print(method_one(c))