# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03_生成练习.py
@Time:NAME.py@Time:2020/7/10 上午9:10
"""
# 生成0-1000数字
# 正常方法


def num(a):
    # i = 0
    for i in range(a):
        print(i)
        i += 1


num(10)
print('_' * 20)

# yield


def scq(a):
    while True:
        for i in range(a):
            yield i
            i += 1


a = scq(5)
for m in range(5):
    print(next(a))
    m += 1
