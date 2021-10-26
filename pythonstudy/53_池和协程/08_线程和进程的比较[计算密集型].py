# 尽管python的多线程无法利用电脑得多核优势，但是对于某些程序，使用多线程还是由于多进程的
# 对于计算密集型：
    # 使用多进程优于多线程
# 所谓IO密集型任务：
    # 是指磁盘IO、网络IO占主要的任务，计算量很小。比如请求网页、读写文件等。
    # 当然我们在Python中可以利用sleep达到IO密集型任务的目的。使用多线程优于多进程，因为减少了进程创建关闭得资源时间

import time
from multiprocessing import Process
from threading import Thread


def math_func(a):
    for i in range(1, 10000000):
        a += i
    print(a)
    return a


if __name__ == '__main__':
    start = time.time()
    # process_l = []
    # for i in range(1, 5):
    #     process_l.append(Process(target=math_func, args=(i,)))
    # for j in process_l:
    #     j.start()
    # for k in process_l:
    #     k.join()
    # end = time.time()
    # print(f'time=>>>{end-start}')   # 使用多进程，时间为：1.3296537399291992
    thred_l = []
    for i in range(1, 5):
        thred_l.append(Thread(target=math_func, args=(i,)))
    for j in thred_l:
        j.start()
    for k in thred_l:
        k.join()
    end = time.time()
    print(f'time=>>>{end - start}')  # 使用多线程，时间为：3.629098415374756
