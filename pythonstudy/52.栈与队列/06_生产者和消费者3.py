# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:06_生产者和消费者3.py
@Time:NAME.py@Time:2021/3/16 16:09
"""
"""
避免阻塞的另一种方法：
    使用JoinableQueue
逻辑：
    每当往队列中插入数据时，队列中存在一个计数器将+1，每当调用一次task_done()时，计数器将-1，直到计数器为0时，将会调用q.join()，才会往下执行
特性：
    q.task_done()：消费者使用此方法发出信号，表示q.get()的返回项目已经被处理。
    q.join()：生产者调用此方法进行阻塞，等待队列中所有的数据被取完；阻塞将持续到队列中的每个项目均调用q.task_done（）方法为止。
注意点：
    q.join()如果能够执行了，意味着队列已经为空，全部处理完毕，因此此时子进程应该和主进程一起关闭，所以在消费者的进程中，deamon应该为true
"""

from multiprocessing import Process, JoinableQueue
import time


# 消费者方法
def consumer(q, name):
    while True:
        res = q.get()
        print(f'{name}消费者结束')
        print("%s 吃了 %s" % (name, res))
        # 每消费一个，执行一次task_done()
        q.task_done()


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
    q = JoinableQueue()
    # 创建生产者
    p1 = Process(target=producer, args=(q, "厨师", "包子"))
    p2 = Process(target=producer, args=(q, "厨师", "饺子"))
    # 设置消费者进程为守护主线程，当q.join()执行的时候，消费者进程同时结束
    c1 = Process(target=consumer, args=(q, "peter1",), daemon=True)
    c2 = Process(target=consumer, args=(q, "peter2",), daemon=True)
    p1.start()
    p2.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()

    # 当task_done()为空时，执行q.join()结束队列
    q.join()

    print('主进程')
