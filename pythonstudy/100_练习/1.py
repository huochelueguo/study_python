# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:1.py
@Time:NAME.py@Time:2020/11/21 16:23
"""


def turn(num):
    if not isinstance(num, int):  # 判断是否为str
        return TypeError("请输入数字")
    if -10 < num < 10:  # 如果为一位数字，直接返回
        return num
    num_int = str(num)  # 转换为str
    if num_int[0] != '-':
        return int(num_int[::-1])
    else:
        num = '-' + num_int[1::][::-1]  # 切片：使用[1::]排除负号再进行切片
        return int(num)
    # return int('-' + num_int[1::][::-1])


print(turn('1a'))
print(turn([1, 2, 3]))
print(turn(-2))
print(turn(23))
print(turn(-123))
