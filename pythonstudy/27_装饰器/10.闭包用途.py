# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:10.闭包用途.py
@Time:NAME.py@Time:2021/4/9 18:57
"""
"""
多次调用某一个函数时，可以只传一次参数，后面不需要多次传参
"""


def bibao(name):
    def send():
        print(f'{name} send hello to you')
    return send


test = bibao('paul')
test()
test()
test()
print('*' * 100)
# 上面使用闭包不需要每次传入参数，否则如下


def send(name):
    print(f'{name} send hello to you')


send('paul')
send('paul')
send('paul')