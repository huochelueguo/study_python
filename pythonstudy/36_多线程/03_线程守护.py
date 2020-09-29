# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03_线程守护.py
@Time:NAME.py@Time:2020/9/27 20:24
"""

import threading
import time


def cook(**kwargs):
    for keys in kwargs:
        print(f'做{kwargs[keys]}吃')
        time.sleep(4)


def eat():
    for i in range(3):
        print('吃东西')
        time.sleep(4)


if __name__ == '__main__':
    food = {'1': 'beef', '2': 'fish', '3': 'chicken'}
    t1 = threading.Thread(target=cook, kwargs=food)
    # 守护主线程方法1，创建时设置
    t2 = threading.Thread(target=eat, daemon=True)
    # 守护主线程方法2，运行前设置
    t1.setDaemon(True)
    t1.start()
    t2.start()
    time.sleep(1)
    print('主线程结束')
    # 由于没有主线程守护，因此主线程需要等待子线程结束后，才结束运行
    # 设置守护主线程后，输出一次后程序结束