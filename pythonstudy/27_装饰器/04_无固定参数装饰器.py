# 装饰器的传参使用 *args **kwargs
import time


def add_time(func):
    # func代表原函数，wrapper代表装饰器中函数，使用*args, **kwargs接不固定参数
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        use_time = (end_time-start_time) * 1000
        print(f'执行函数消耗时间为: {use_time} 毫秒')
    return wrapper


@add_time
def f(a, b):

    print("函数1，功能为两个数字求和")
    time.sleep(1)
    print(f'a + b ={a + b}')


@add_time
def f2(a, b, c):

    print('函数2，功能为三个数字求和')
    time.sleep(3)
    print(f'a + b + c = {a+b+c}')


if __name__ == '__main__':
    f(99, 200)
    print('_' * 20)
    f2(10, 20, 30)

