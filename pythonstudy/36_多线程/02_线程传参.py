# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_线程传参.py
@Time:NAME.py@Time:2020/9/27 16:28
"""
# 在线程中传递参数
import threading
import time


def cook(food):
    print(f'正在做:{food}')


def clean_room(*args):
    for i in range(2):
        print(f'开始清理 {room[i]}')
        time.sleep(3)
        print('清理完毕')


def wash_clothes(**kwargs):
    # kwargs的遍历
    for keys in kwargs:
        print(f'开始洗 {kwargs[keys]} 的衣服')
        time.sleep(3)
        print('洗完')


if __name__ == '__main__':
    room = ('卧室', '客厅')
    clothes = {'0': 'father', '1': 'mother'}
    # 传入参数为元组时，参数名称为args
    # 传入参数为字典时，参数名称为kwargs
    t0 = threading.Thread(target=cook, args=('beef', ))
    t1 = threading.Thread(target=clean_room, args=room)
    t2 = threading.Thread(target=wash_clothes, kwargs=clothes)
    t0.start()
    t1.start()
    t2.start()

