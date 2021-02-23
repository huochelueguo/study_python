# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:11_解决死锁.py
@Time:NAME.py@Time:2021/2/23 17:42
"""
"""
解决死锁的方式：
1.一个线程有多个锁时，使用顺序保持一致
2，一个线程有多个锁时，尽量不要交叉使用锁，使用完成后尽快解锁，再去使用另一个锁
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
    lock_eat.acquire()
    print('eat中拿到eat锁')
    time.sleep(1)
    lock_wash.acquire()
    print('eat中拿到wash锁')
    num += 1
    lock_eat.release()
    print('eat中解开eat锁')
    lock_wash.release()
    print('eat中解开wash锁')

# 两个函数中各调用了2个锁，但是2个锁的顺序一致，因此不会出现死锁


if __name__ == '__main__':
    for i in range(2):
        t1 = Thread(target=wash, daemon=False)
        t2 = Thread(target=eat, daemon=False)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print('-' * 10)