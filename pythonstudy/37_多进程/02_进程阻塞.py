import time
import random
from multiprocessing import Process


def speak(words):
    time.sleep(random.randrange(2, 5))
    print(f'我要开始说了{words}')
    time.sleep(random.randrange(1,5))
    print('说完啦')


# 正常情况下，主进程应该再子进程中执行，使用了join得进程阻塞， 将主进程再子进程执行完成后再执行
if __name__ == '__main__':
    p1 = Process(target=speak, args=('123',))
    p2 = Process(target=speak, args=('abc',))
    p3 = Process(target=speak, args=('$#$@#$%',))
    p = [p1, p2, p3]
    for i in p:
        i.start()
    for j in p:
        j.join()
    print('我是主进程')