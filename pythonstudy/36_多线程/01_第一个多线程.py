# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_第一个多线程.py
@Time:NAME.py@Time:2020/9/27 16:06
"""

import threading
import time


def clean_room():
    print('打扫卫生')
    time.sleep(5)
    print('打扫完成')


def wash_clothes():
    print('洗衣服')
    time.sleep(5)
    print('洗完')


if __name__ == '__main__':

    # 正常需要打扫结束才可以洗衣服，需要10s+
    # clean_room()
    # wash_clothes()

    # 使用多线程，两个方法可以同时启动，时间需要5+
    # 创建线程，注意：target的目标不需要带括号
    t1 = threading.Thread(target=clean_room)
    t2 = threading.Thread(target=wash_clothes)
    # 启动线程
    t1.start()
    t2.start()
