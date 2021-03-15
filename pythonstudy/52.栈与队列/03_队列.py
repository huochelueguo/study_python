# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03_队列.py
@Time:NAME.py@Time:2021/3/12 18:19
"""

"""
概念：
    只允许在一段进行插入操作，而在另一端进行删除操作的线性表
特点：
    先进先出，不允许对中间元素进行修改
    插入和删除操作有时称为入队（enqueue）和出队（dequeue）
    与列表或数组不同，队列通常不允许随机访问所包含的对象。
作用：
    解耦：使程序直接实现松耦合，修改一个函数，不会有串联关系。
https://www.cnblogs.com/dbf-/p/11118628.html
http://linuxeye.com/334.html
"""

from queue import Queue

q = Queue(maxsize=12)    # maxsize值≤0时，该队列长度无限制，否则为设置值
q.put(4, block=False)    # 向队列中插入值,共有2个参数，第一个为插入值，第二个为block，默认为true，插入出现阻塞则等待；如果为false，插入出现阻塞则报错queue.Full
q.put(5, block=False)
print(q.qsize())    # 输出队列大小（实际内容）
print(q.empty())    # 输出队列是否为空
print(q.full())     # 输出队列是否已满
print(q.get())
print(q.get())
print(q.get(block=True))   # 从队列中取值，参数block默认为true，空队列在获取时也不会报错；改为false，则会抛出错误
