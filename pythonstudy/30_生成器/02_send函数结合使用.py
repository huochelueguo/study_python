# send()可以给函数发送一个参数:
# 注意在使用send（）向生成器发送数据时，首先要使用next()或者send(None),否则会报错


def foo():

    print(f'starting')
    while True:
        a = yield 666
        print(f'a:{a}')


g = foo()
print('-' * 50)
print(next(g))
print('-' * 50)
print(next(g))
print('-' * 50)
# 不同于next,通过send可以将参数传入，因此a的值为888，不是none
print(g.send(888))
