# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:08.send&next.py
@Time:2021/4/22 上午9:20
"""
"""
send和next的区别：
    next 只能取值
    send 既能取值也能发送值
send注意点：
    1。第一个send不能发送值，只能发送send(None)或者先调用一下next（）
    2。最后一个yeild无法接受send发送的值
"""

def scq():
    a =1
    while a < 5:
        s = yield 200
        a +=1
        print(a)
        print(f's is {s}')


s =scq()
# print(s.send(444))    # 第一步不能使用send,需要使用next走到生成器yield处
print(next(s))  # yield将200返回后停止，还未给s赋值：输出200 a=1
print(next(s))  # 接着上一步，s被赋值为空，接着输出s is None，在走到yield处，将200返回停止：输出s is None 和200 a=2
print(next(s))  # 同上 a =3
print(s.send(666)) # 虽然200被返回，但是send传入了一个值，因此s被赋值为666，输出s is 666，再次到yield处停止 a= 4
# print(s.send(22))