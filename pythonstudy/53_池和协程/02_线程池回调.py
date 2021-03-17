# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_线程池回调.py
@Time:NAME.py@Time:2021/3/17 15:58
"""

"""
回调的作用：因为线程池的result()获取结果时会阻塞主线程，影响效率，
        因此可通过 Future 的 add_done_callback() 方法来添加回调函数，该回调函数形如 fn(future)。
        当线程任务完成后，程序会自动触发该回调函数，并将对应的 Future 对象作为参数传给该回调函数。
和result区别：result为同步调用效率较低，add_done_callback()为异步调用
使用方法：
    将每次submit后的结果存入一个列表中，循环列表，对每一个值调用add_done_callback()函数，该函数参数为回调函数，再回调函数中获取reslut
    
"""
import time
from concurrent.futures import ThreadPoolExecutor


def test1(n):
    time.sleep(2)
    print(f'第{n}次执行')
    return n * n


def call_back(future):  # 异步调用的函数，可以在函数中使用futurn.result()获取的结果
    nums = future.result()
    print(nums)


if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=5)
    result = []
    for i in range(20):
        res = pool.submit(test1, i)
        result.append(res)
    for j in result:
        j.add_done_callback(call_back)  # 调用异步调用函数，注意这里的参数即回调函数名称，没有回调函数的参数
    pool.shutdown()
    # print(result)
    print('-' * 20)
"""
输出：
第1次执行第0次执行

0
1
第4次执行
第3次执行
9
16
第2次执行
4
第6次执行
36
第5次执行
25
第7次执行
49
第9次执行第8次执行
64

81
第11次执行
第10次执行
100
121
第14次执行
196
第12次执行
144第13次执行
169

第16次执行第15次执行
225

256
第19次执行
361
第18次执行
第17次执行
324
289
"""