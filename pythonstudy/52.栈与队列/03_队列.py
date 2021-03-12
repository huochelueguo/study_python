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
https://geek-docs.com/python/python-examples/python-queue-first-in-first-out.html
http://c.biancheng.net/view/2624.html
"""

from queue import Queue

q = Queue()
print(q, type(q))
q.put(4)
q.put(5)
print(q.get())
