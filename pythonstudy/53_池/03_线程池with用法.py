# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03_线程池with用法.py
@Time:NAME.py@Time:2021/3/17 17:04
"""
"""
线程池实现了上下文管理协议（Context Manage Protocol），因此，程序可以使用 with 语句来管理线程池，这样即可避免手动关闭线程池
使用方法类似于打开文件
"""
from concurrent.futures import ThreadPoolExecutor
import time


def test1(n):
    time.sleep(0.02)
    print(f'当前时间:{time.time()}，第{n}次调用')
    return n * n


def call_back(future):
    res = future.result()
    print(res)


with ThreadPoolExecutor(max_workers=30) as pool:    # 使用with ThreadpoolExecutor() as pool代替了原来的pool.shutdown()
    result = []
    while True:
        for i in range(500):
            pool.submit(test1, i)
            # res = pool.submit(test1, i)
            # result.append(res)
    # for j in result:
    #     j.add_done_callback(call_back)
