# 可以指定装饰器函数wrapper接受和原函数一样的参数


import time


def all_time(func):
    # 装饰器函数和原函数参数一致
    def wrapper(a, b):
        print('装饰器中，函数多了计时功能，先执行装饰器内容')
        start_time = time.time()
        func(a, b)
        end_time = time.time()
        use_time = (end_time - start_time) * 1000
        print(f'执行消耗时间为: {use_time} 毫秒')
        # return
    return wrapper


# 函数本身功能仅为求和
@all_time
def f(a, b):
    print('函数本身')
    time.sleep(1)
    print(f'函数本身仅有求和功能：a + b = {a + b}')


if __name__ == '__main__':
    f (4, 9)

