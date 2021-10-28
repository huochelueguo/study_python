# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_线程池.py
@Time:NAME.py@Time:2021/3/17 14:19
"""
"""
同步：接口发送请求给服务端时，一直等待服务端返回数据，未返回之前，不做任何事情
异步：接口发送请求给服务端时，不会等待返回结果就进行后续操作
"""

"""
http://c.biancheng.net/view/2627.html
https://www.cnblogs.com/tashanzhishi/p/10775641.html
线程池：
    概念：系统启动时就会按照设置线程数创建N个线程，程序只要将函数提交给线程池，线程池就会选择一个空闲线程来处理该函数，处理完成后，该线程不停止，而是
        转为空闲状态，等待下一个函数过来
    好处：
        1.相对于多线程，节省时间和资源
        2.因为有设置的最大线程数，保护了计算机硬件，不会出现线程过多导致系统性能下降
        3.对应IO密集型任务可以通过创建线程池来提高效率，而对于计算密集型则没必要，计算密集型可以考虑分布式计算。
    线程池整体逻辑：
        1.调用 ThreadPoolExecutor 类的构造器创建一个线程池。
        2.定义一个普通函数作为线程任务。
        3.调用 ThreadPoolExecutor 对象的 submit() 方法来提交线程任务。
        4.当不想提交任何任务时，调用 ThreadPoolExecutor 对象的 shutdown() 方法来关闭线程池。
    基本使用：
        1.引入线程池：from concurrent.futures import ThreadPoolExecutor   
        2.创建线程池：pool = ThreadPoolExecutor(max_workers=5)
            max_workers：线程池中线程数，有默认值，默认为cpu数量*5
        3.向线程池提交任务：pool.submit(函数名,参数)
        4.关闭线程池：pool.shutdown()
            wait=True，等待池内所有任务执行完毕回收完资源后才继续
            wait=False，立即返回，并不会等待池内的任务执行完毕
        5.获取返回值：res = pool.submit().result()
            注意：result()会产生阻塞，但该方法会阻塞当前主线程，只有等到钱程任务完成后，result() 方法的阻塞才会被解除，这时候程序为串行
        6.回调函数:add_done_callback(fn)
"""

import time
from concurrent.futures import ThreadPoolExecutor


def produce(n):
    time.sleep(2)
    print(f'输出{n}')
    return n * n


if __name__ == '__main__':
    result = []
    pool = ThreadPoolExecutor(max_workers=5)  # 创建线程池
    for i in range(20):
        res = pool.submit(produce, i)  # 向线程池提交任务
        result.append(res)     # 异步获取线程返回值，函数为空返回为None
        # result.append(res.result())   # 这样影响效率
    pool.shutdown()
    for j in result:
        print(j.result())
