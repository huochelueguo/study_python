# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:04_线程锁.py
@Time:NAME.py@Time:2020/9/29 15:45
"""
import threading
from threading import Lock

g_num = 0
lock = Lock()


def add1():
    global g_num
    for i in range(100000):
        lock.acquire()
        g_num = g_num + 1
        lock.release()


def add2():
    global g_num
    for i in range(100000):
        lock.acquire()
        g_num = g_num + 1
        lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=add1)
    t2 = threading.Thread(target=add2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # 两个add共用了一个全局变量，因此调用时可能出现数据错误的情况，这时候应该在可能出现问题的函数中加锁
    print(g_num)
