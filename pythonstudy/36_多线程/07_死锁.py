# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:07_死锁.py
@Time:NAME.py@Time:2021/1/12 18:23
"""
import time
from threading import Thread, Lock

num = 0
lock_eat = Lock()
lock_wash = Lock()


def wash(n=None):
    # for i in range(n):
        global num
        lock_eat.acquire()
        lock_wash.acquire()
        num += 1
        print('在wash中给eat上锁')
        lock_eat.release()
        lock_wash.release()


def eat(n=None):
    # for i in range(n):
        global num
        lock_wash.acquire()
        time.sleep(1)
        lock_eat.acquire()
        time.sleep(5)
        num += 1
        print('在eat中给wash上锁')
        lock_wash.release()
        lock_eat.release()


if __name__ == '__main__':
    t1 = Thread(target=wash, args=(3,), daemon=False)
    t2 = Thread(target=eat, args=(3,), daemon=False)
    for i in range(3):
        t1.start()
        t2.start()