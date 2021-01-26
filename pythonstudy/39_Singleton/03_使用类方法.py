# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03_使用类方法.py
@Time:NAME.py@Time:2021/1/26 18:37
"""
import time
from threading import Thread, Lock

class Singelton(object):
    _singel = None

    def __init__(self):
        time.sleep(1)

    @classmethod
    def singer(cls):
        if cls._singel is None:
            cls._singel = super()
        return cls._singel


class Singel_lock(object):
    _singel = None
    with_lock = Lock()

    def __init__(self):
        time.sleep(0.1)

    @classmethod
    def singer(cls):
        with cls.with_lock:
            if cls._singel is None:
                cls._singel = cls()
        return cls._singel


def task():
    obj = Singelton().singer()
    print(obj)


def task2():
    obj2 = Singel_lock().singer()
    print(obj2)


if __name__ == '__main__':
    """
        l1 = []
        for i in range(3):
            i = Thread(target=task)
            l1.append(i)
        for i in l1:
            i.start()
            i.join()
        print('main_thred')
    
    
    输出：
    <__main__.Singelton object at 0x01BD3EF8>
    <__main__.Singelton object at 0x01BD3EC8>
    <__main__.Singelton object at 0x01BD3EB0>
    main_thred
    存在问题：多线程时，由于时间差，导致可能出现多次创建实例，因此需要枷锁
    """
    l1 = []
    for i in range(3):
        i = Thread(target=task2)
        l1.append(i)
    for i in l1:
        i.start()
        i.join()
    print('main_thred')
    # task2()