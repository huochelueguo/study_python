# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:12.信号量.py
@Time:2021/5/27 上午9:17
"""

"""
信号量（segmaphore）的作用：
    当多线程同时存在多个IO时，服务器可能无法承受该冲击造成宕机；此时可以使用信号量，设置一个计数器功能，保证同一个时间仅有有限定线程访问
    segmaphore为一个数值，每relase一次+1，acquire一次-1，当值为负数时将会报错,当为0时将会暂停后续线程，等待其他relase释放
使用方法：
    1. 定义一个信号量 sm = threading.Semaphore(max workers)
    2. 在要使用信号量的函数上增加加解锁，也可以直接使用with sm:
"""

import threading
import random
import time

sm = threading.Semaphore(3)


def worker():
    with sm:
    # sm.acquire()    # 使用了sm进行了加锁和解锁后，每次只有3个线程，防止线程过多造成阻塞
        print('开始工作')
        time.sleep(random.randint(1, 4))
        print('工作完成')
    # sm.release()


if __name__ == '__main__':
    thread = []
    for i in range(10):
        thread.append(threading.Thread(target=worker))

    for j in thread:
        j.start()
