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


def wash():
    global num
    lock_eat.acquire()
    print('wash中拿到eat锁')
    lock_wash.acquire()
    print('wash中拿到wash锁')
    num += 1
    lock_eat.release()
    print('wash中解开eat锁')
    lock_wash.release()
    print('wash中解开wash锁')


def eat():
    global num
    lock_wash.acquire()
    print('eat中拿到wash锁')
    time.sleep(1)
    lock_eat.acquire()  # wash第一次执行完成后，再第一次执行eat时，由于有一个sleep，导致第二次执行wash时抢先把eat锁了，因此eat中无法给eat上座
    print('eat中拿到eat锁')
    num += 1
    lock_wash.release()
    print('eat中解开wash锁')
    lock_eat.release()
    print('eat中解开eat锁')


if __name__ == '__main__':
    for i in range(2):
        t1 = Thread(target=wash, daemon=False)
        t2 = Thread(target=eat, daemon=False)
        t1.start()
        t2.start()
        print('-' * 10)

