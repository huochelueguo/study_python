# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:04_生产者和消费者.py
@Time:NAME.py@Time:2021/3/12 18:40
"""
"""
使用队列模拟一个生产者和消费者模型，多线程A不断生产数据存入队列中，多线程B再队列中获取数据；防止出现某端处理阻塞导致整个流程卡死，解决生产者和消费者的强耦合问题
https://www.jianshu.com/p/e50b9e4ce5aa
"""

import queue
import time
import random
from threading import Thread

q = queue.Queue(maxsize= 200)


def procduer(nums, name):
    count = 0
    while count < nums:
        print('制作中...')
        time.sleep(random.randint(1, 4))
        q.put(count)
        print(f'完成第{count+1}个{name}制作')
        count += 1


def consumer(nums, name):
    count = 0
    while count < nums:
        print('消费中')
        time.sleep(random.randint(1, 5))
        q.get()
        print(f'消费的第{count+1}个{name}')
        count += 1


if __name__ == '__main__':

    p1 = Thread(target=procduer, args=(10, '包子'))
    c1 = Thread(target=consumer, args=(10, '包子'))
    p1.start()
    c1.start()


