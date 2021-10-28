# 进程池除了可以使用 multiprocessing中得pool以外，也可以使用concurent.future中的ProcessPoolExecutor

import time
from concurrent.futures import ProcessPoolExecutor


def work(n):
    print(f'{n}==>time to go')
    time.sleep(1)
    return n * n


if __name__ == '__main__':
    start = time.time()
    p = ProcessPoolExecutor(max_workers=4)
    res_l = []
    for i in range(1, 10):
        # 将x.submit(func, x)返回值收集起来，当进程池执行完成后再一起读取，这样为异步，节约时间
        obj = p.submit(work, i)  # 相当于apply_async()同步方法
        res_l.append(obj)
    p.shutdown()    # 相当于close和join方法，关闭池并且主进程阻塞
    
    for j in res_l:
        print(j.result())
    end = time.time()
    use_time = end - start
    print(f'end==>{use_time}')  # 异步的情况下，时间为3.1976406574249268
