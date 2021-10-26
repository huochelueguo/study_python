import os
import time
import random
from multiprocessing import Pool


# 主要还是使用concurent.future模块来实现池，参考53_池和携程

def work(n):
    print('%s run' %os.getpid())
    time.sleep(random.randrange(0, 3))
    return n**2


if __name__ == '__main__':
    p = Pool(3)
    res_l = []
    for i in range(5):
        # 该代码为非阻塞调用，一共有三个进程，因此先执行了前三个数据，执行完成后继续去池中找数据，完成剩余2个数据，因此pid会有相同得
        # 也因为非阻塞调用，因此每一个进程不需要等到work函数结束就可以执行，否则将会按顺序每个执行work后后面才能执行
        res = p.apply_async(work, (i,))
        res_l.append(res)

    print('start')
    p.close()
    p.join()
    print('main Process is ending')
    print(res_l)
    # 对于非阻塞进程池，对于结果可以使用x.get()方法获取调用函数得返回值，阻塞进行池不具有该方法
    for j in res_l:
        print(j.get())