# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:05_生产者和消费者2.py
@Time:NAME.py@Time:2021/3/16 14:20
"""
"""
    # 问题1：生产者生产完了，没有向消费者发送一个停止的信号，所以消费者一直会一直阻塞在q.get()，导致程序无法退出。
    # 解决办法，主线程中，向队列中插入特殊字符，消费者获取到该值即break；需要注意的是，有几个消费者，就要插入几个特殊值
"""


from multiprocessing import Process, Queue
import time


# 消费者方法
def consumer(q, name):
    while True:
        res = q.get()
        if res is None:
            break
        else:
            print(f'{name}消费者结束')
        print("%s 吃了 %s" % (name, res))


# 生产者方法
def producer(q, name, food):
    for i in range(3):
        time.sleep(1)  # 模拟生产的时间延迟
        res = "%s %s" % (food, i)
        print("%s 生产了 %s" % (name, res))
        # 把生产的放入到队列中
        q.put(res)


if __name__ == "__main__":
    # 创建队列
    q = Queue()
    # 创建生产者
    p1 = Process(target=producer, args=(q, "厨师", "包子"))
    p2 = Process(target=producer, args=(q, "厨师", "饺子"))
    c1 = Process(target=consumer, args=(q, "peter1",))
    c2 = Process(target=consumer, args=(q, "peter2",))
    p1.start()
    p2.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    q.put(None)
    q.put(None)
    print('主进程')


