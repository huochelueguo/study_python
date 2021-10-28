# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:04_线程池map.py
@Time:NAME.py@Time:2021/3/17 17:22
"""
"""
map的作用：
     map(func, *iterables, timeout=None, chunksize=1) 方法，
     该方法的功能类似于全局函数 map()，区别在于线程池的 map() 方法会为 iterables 的每个元素启动一个线程，以并发方式来执行 func 函数。
     这种方式相当于启动 len(iterables) 个线程，井收集每个线程的执行结果。
优点：
    1.代码简洁，直接替代了原来的pool.submit()和add_done_callback()，实现了调用线程池并且异步返回结果
使用方法：
    result = pool.map(函数, 数据)
"""
from concurrent.futures import ThreadPoolExecutor
import time


def teest1(n):
    time.sleep(2)
    print(f'第{n}次调用')
    return n * n


with ThreadPoolExecutor(max_workers=10) as pool:
    result = pool.map(teest1, [i for i in range(20)])
    for i in result:
        print(i)