# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_gevent.py
@Time:2021/5/19 上午9:31
"""

from gevent import spawn
from gevent import monkey
monkey.patch_all()
import gevent
import time
"""
进程：资源单位
线程：执行单位
协程：
    主要作用：在单线程中实现并发
    协程使用技术：多道技术，切换+保存状态
        切换的情况：遇到IO或者长时间占用
    使用模块：
结论：
    1.使用协程能够压缩时间，减少资源的占用
    2.在协程中，某一个函数存在IO或者被占用时，线程就会切换到其他函数执行，在适当的时机在切换回来继续执行，循环往复，给系统造成一种不停顿的感觉
    3.协程中耗时即该协程中最大函数运行时间       
"""



def heng():
    print('哼')
    time.sleep(2)
    print('哼')


def ha():
    print('哈')
    time.sleep(3)
    print('哈')


def call_back(r):
    print((1))
    print(r.result)


start_time = time.time()
# heng()
# ha()
g1 = spawn(heng)  # 查看源码得知spwn会自动调用start，类似多线程的启动
g2 = spawn(ha)
g1.add_spawn_callback(call_back)
g1.join()  # 因此可以使用join()方法，来制造类似线程阻塞，最后再执行主线程的print
g2.join()

# 以上两个可以简写为下面代码
# gevent.joinall([g1, g2])
# 获取返回值也可以使用gx.value

print(f'时间是：{time.time() - start_time}')
