# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:06.带参数得装饰器.py
@Time:NAME.py@Time:2020/11/5 16:54
"""
# 作用：比如说输出日志时，根据装饰器参数，输出不同等级得日志信息


def log(level):
    def log_level(func):
        def warpper():
            if level == 'info':
                print('1')
                func()
            if level == 'error':
                print('2')
                func()
        return warpper
    return log_level


@log(level='info')
def info_level():
    print('info')


@log(level='error')
def error_level():
    print('error')


info_level()
error_level()
# 输出1
# info
# 2
# error