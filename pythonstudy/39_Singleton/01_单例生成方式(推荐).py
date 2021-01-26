# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_单例生成方式(推荐).py
@Time:2021/1/26 上午9:21
"""
# 改写__new__，每次返回同一个实例
import threading


class Singel(object):

    _single = None  # 定义一个类属性
    _obj = None

    def __new__(cls, *args, **kwargs):
        if cls._single is None:     # 调用类属性，需要使用类名.类属性的方法
            cls._single = super().__new__(cls)  # 给_single赋值
            print(cls._single)
        return cls._single

    def __init__(self, name):
        self.name = name


def task():
    task1 = Singel(2)
    print(task1)


if __name__ == '__main__':
    # a = Singel('a')
    # b = Singel('b')
    # print(a)
    # print(b)
    l1 = []
    for i in range(100):
        i = threading.Thread(target=task)
        l1.append(i)
    for j in l1:
        j.start()
