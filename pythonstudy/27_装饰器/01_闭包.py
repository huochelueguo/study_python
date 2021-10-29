# 闭包：在函数中再嵌套一个函数，并且引用外部函数的变量，这就是一个闭包了
"""
闭包：
    概念：
        闭 函数指的是该函数为内嵌函数
        包 函数指该函数包含对外层函数作用于名字的引用（不是对全局函数）
    核心：
        名字查找关系以函数定义阶段为准
    执行闭包：
        先使用参数a=闭包函数()，将闭包函数内部函数地址赋值给参数a
        执行a()，即执行了闭包函数
    特点：
        1、正常情况下，一个函数得对象执行完成后，将会释放内存，而闭包函数因为拥有对内函数得引用，因此不会释放
        2、内函数得引用再函数得定义阶段，因此外部定义得数据不会改变内函数得值
"""


# 正常情况下，函数参数只能通过外部传入
def func(n):
    print('this is normal func')
    return n * n


a = func(5)
print(a)
print('-' * 50)


# 使用闭包得情况下，函数的参数可以通过外函数赋值给他，同时对于外部的全局变量来说，无法影响到内函数得值
# 因为再外函数内部定义了m为1000，又因为闭包函数得数据引用再函数得定义阶段。因此就算外部m为66.66，也不会去使用
# oo(99)相当于inner(99)


def outter(m):
    m = 1000

    def inner(n):
        print('this is inner func')
        print(f'm==>{m}')
        print(f'n==>{n}')
        return n * m

    return inner


m = 66.66
oo = outter(50)
print(oo(99))
print('-' * 50)


# 同时，再其他函数中，还能调用该内函数
def aa():
    print('其他函数中调用内函数')
    return oo(1000)


print(aa())
