# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:05_线程阻塞.py
@Time:NAME.py@Time:2020/9/29 16:02
"""
import time
import threading


def work():
    for i in range(10):
        print('子线程运行中')
        time.sleep(2)


if __name__ == '__main__':
    t1 = threading.Thread(target=work)
    t1.start()

    # 如果想让主线程内容，在子线程结束后再执行，那么可以使用线程.join()；注意在启动后在join
    t1.join()
    time.sleep(0.5)
    print('主线程结束')