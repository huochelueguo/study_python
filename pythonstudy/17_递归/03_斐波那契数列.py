# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03_斐波那契数列.py
@Time:NAME.py@Time:2020/7/25 上午9:18
"""
# 输入数字N，输出第N位的值，使用递归的方法


def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        m = f(n - 2) + f(n - 1)
        return m


def f2(n):
    list2 = []
    for i in range(n):
        if i == 0 or i == 1:
            list2.append(1)
        else:
            list2.append(list2[i - 2] + list2[i - 1])
    return list2


if __name__ == '__main__':
    print(f(1))
    print(f(2))
    print(f(3))
    print(f(4))
    print(f2(13))
    lis = []
    for a in range(1, 12):
        lis.append(f(a))
    print(lis)


