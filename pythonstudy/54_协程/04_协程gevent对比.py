from gevent import spawn
from gevent import monkey
monkey.patch_all()
import time


def task(n, m):
    time.sleep(0.2)
    print(f'n*n==>{int(m*m)}', end='    ')
    print(f'n*n==>{int(n*n)}')


def single():
    for i in range(10):
        task(i, i+1)


def xeicheng():
    li = []
    for i in range(10):
        li.append(spawn(task, i, i+1))
    for j in li:
        j.join()


if __name__ == '__main__':
    time0 = time.time()
    print('单线程开始')
    single()
    time2 = time.time()
    print(f'单线程结束，使用时间为:{time2-time0}')  # 使用时间为:2.062837600708008
    print('协程开始')
    xeicheng()
    time3 = time.time()
    print(f'协程结束，使用时间为：{time3-time2}')  # 使用时间为：0.20391464233398438
