# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:10_多个线程争夺资源.py
@Time:NAME.py@Time:2021/2/23 17:21
"""

"""
多个线程争夺同一个资源时，有可能造成该资源值错误
如下：每次输出内容不一致，就是因为两个函数共同修改num导致，因此需要枷锁

"""
import time
from threading import Thread, Lock

num = 0
lock1 = Lock()


def test1():
    global num
    for i in range(100000):
        num += 1
        # time.sleep(0.01)


def test2():
    global num
    for i in range(100000):
        num += 1
        # time.sleep(0.01)


if __name__ == '__main__':
    t1 = Thread(target=test1)
    t2 = Thread(target=test2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)
