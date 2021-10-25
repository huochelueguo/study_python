import time
import random
from multiprocessing import Process


def speak(words):
    time.sleep(random.randrange(2, 5))
    print(f'我要开始说了{words}')
    time.sleep(random.randrange(1,5))
    print('说完啦')


# 当子进程的daemon是true时，主进程结束后，子进程也将会结束
if __name__ == '__main__':
    p1 = Process(target=speak, args=('123',), daemon=True)
    p2 = Process(target=speak, args=('abc',), daemon=True)
    p3 = Process(target=speak, args=('$#$@#$%',), daemon=True)
    p1.start()
    p2.start()
    p3.start()
    time.sleep(4)
    print('我是主进程，要结束啦')