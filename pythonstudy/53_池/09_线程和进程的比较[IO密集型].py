# 以下代码为IO密集型讲解，使用多线程能够减少系统开销

import time
from threading import Thread
from multiprocessing import Process
import os


def io_func(n):
    time.sleep(3)
    print(f'{n} is end==》使用端口是：{os.getpid()}')


if __name__ == '__main__':
    start = time.time()
    # thred_l = []
    # for i in range(1, 5):
    #     thred_l.append(Thread(target=io_func, args=(i,)))
    # for j in thred_l:
    #     j.start()
    # for k in thred_l:
    #     k.join()
    # end = time.time()
    # print(f'time=>>>{end - start}')  #  多线程得情况下时间为3.030141830444336
    process_l = []
    for i in range(1, 5):
        process_l.append(Process(target=io_func, args=(i,)))
    for j in process_l:
        j.start()
    for k in process_l:
        k.join()
    end = time.time()
    print(f'time=>>>{end-start}')   # 使用多进程，时间为：3.1766836643218994