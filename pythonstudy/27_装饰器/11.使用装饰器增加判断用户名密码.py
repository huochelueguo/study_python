# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:11.使用装饰器增加判断用户名密码.py
@Time:2021/4/15 下午11:31
"""


def auth(func):
    def wrapper(*args, **kwargs):
        name = input('请输入用户名：')
        pwd = input('请输入密码：')
        if name == '小明' and pwd == '123':   # 使用装饰器对函数增加一个判断
            res = func(*args, **kwargs)
            return res
        else:
            print('error')
    return wrapper


@auth
def hello(name):
    print(f'欢迎{name}')


hello('小明')