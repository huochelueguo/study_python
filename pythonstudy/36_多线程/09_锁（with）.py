# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:09_锁（with）.py
@Time:NAME.py@Time:2021/1/26 18:15
"""

"""
with+锁的作用：代替lock.acquire()和lock.release()，实现自动解锁
"""

from threading import Thread, Lock

lock_with = Lock()
g_num = 0


def add1():
    global g_num
    for i in range(100000):
        with lock_with:
            g_num += 1


def add2():
    global g_num
    for i in range(100000):
        with lock_with:  # 等同于lock.qcquire()和lock.release()
            g_num += 1


if __name__ == '__main__':
    a = Thread(target=add1)
    b = Thread(target=add2)
    l1 = [a, b]
    for i in l1:
        i.start()
        i.join()
    print(g_num)