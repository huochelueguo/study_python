import time
import random
from multiprocessing import Process


def speak(words):
    time.sleep(random.randrange(2, 5))
    print(f'我要开始说了{words}')
    time.sleep(random.randrange(1,5))
    print('说完啦')


# 微软电脑，开启多进程，必须要在main函数之下
if __name__ == '__main__':
    p1 = Process(target=speak, args=('123',))
    p2 = Process(target=speak, args=('abc',))
    p3 = Process(target=speak, args=('$#$@#$%',))
    p1.start()
    p2.start()
    p3.start()