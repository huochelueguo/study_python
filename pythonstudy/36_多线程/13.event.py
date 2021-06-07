# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:13.event.py
@Time:2021/5/28 上午9:04
"""
"""
event事件定义：
    当有多个事件或者多个线程之间有先后关系时，如红绿灯：车辆必须在绿灯的情况下才可以通行，这时候需要借助threading中的
event时间，来控制顺序
event使用方法：
    1. 设置事件：event = threading.Event()
event常用方法：
    1. event.set()  返回值为true,所有等待它成为True的线程都被唤醒。当标志保持在True的状态时，线程调用wait()是不会阻塞的
    2. event.clear() 返回值为false,调用wait()的线程将阻塞，直到另一个线程调用set()将内部标志重新设置为True。
    3. event.wait() 线程阻塞，直到其他线程发来event.set()
    4. event.is_set() 当且仅当内部标志为True时返回True
"""
import threading
import time
import random

# 示例1：实现红灯停绿灯行
event1 = threading.Event()


def light():
    print('light：现在红灯亮起')
    time.sleep(random.randint(2, 5))
    print('light：绿灯亮')
    event1.set()  # event设置为true，底部car可以通过
    time.sleep(random.randint(2, 5))
    event1.clear()  # 红灯后，为false,无法通过


def car(name):
    print(f'car：{name} 等待绿灯通行')
    event1.wait()
    print(event1.is_set())
    print(f'car：{name} 绿灯亮起，开始通过')


light_t = []
car_t = []
for i in range(3):
    light_t.append(threading.Thread(target=light))
    car_t.append(threading.Thread(target=car, args=(1,)))

for j in range(3):
    light_t[j].start()
    car_t[j].start()

# 示例2： 一个列表[1, 2, 3]，另一个[a, b, c]， 输出一个新表[1a, 2b, 3c]
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
