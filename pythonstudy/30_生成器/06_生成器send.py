# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:06_生成器send.py
@Time:NAME.py@Time:2021/3/24 18:09
"""


def send_scq():
    print('begin')
    food_list = []
    while True:
        res = yield food_list
        food_list.append(res)
        print(f'快来吃{food_list}')


# 创建一个生成器
s = send_scq()
# 使用next或者send(none)，使函数挂起在res= yield food_list
# s.send(None)
next(s)

# 执行下面语句时，函数位于res = yield food_list，food_list为空
# 执行下面语句，将鸡赋值给food_list，向下执行print输出，继续循环到yield时，停止执行
s.send('鸡')

s.send('鸭')
