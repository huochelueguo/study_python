# 对于x.submit(func, a)具有.result()方法，可以同步获取返回值，这样比较消耗时间

import time
from concurrent.futures import ThreadPoolExecutor


def work(n):
    print(f'{n}==>time to go')
    time.sleep(1)
    return n * n


if __name__ == '__main__':
    start = time.time()
    res_l = []
    t = ThreadPoolExecutor(max_workers=4)
    for i in range(1, 10):
        obj = t.submit(work, i).result()  # 相当于apply同步方法
        res_l.append(obj)
    for j in res_l:
        print(j)
    t.shutdown()
    end = time.time()
    user_time = end - start
    print(f'end==>{user_time}')  # 同步的情况下，时间为9.117204427719116
