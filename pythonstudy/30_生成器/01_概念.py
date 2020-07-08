# https://blog.csdn.net/mieleizhi0522/article/details/82142856
#
# yield和return的关系和区别了：
# 简要理解：yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后开始
# 带yield的函数是一个生成器，而不是一个函数了，这个生成器有一个函数就是next函数，next就相当于“下一步”生成哪个数
# 这一次的next开始的地方是接着上一次的next停止的地方执行的，所以调用next的时候，生成器并不会从foo函数的开始执行，只是接着上一步停止的地方开始，
# 然后遇到yield后，return出要生成的数，此步就结束


def foo():

    print('starting..')
    while True:
        a = yield 666
        print(f'a = {a}')


# 这一步执行时：因为foo函数中有yield关键字，所以foo函数并不会真的执行，而是先得到一个生成器g(相当于一个对象)
g = foo()
# 调用next方法，foo函数正式开始执行，先执行foo函数中的print方法，
# 然后进入while循环程序遇到yield关键字，然后把yiel当作return,return了一个4之后，程序停止;并没有执行赋值给res操作，此时next(g)语句执行完成
print(next(g))
print('_' * 20)
# 1.这个时候是从刚才那个next程序停止的地方开始执行的，也就是要执行res的赋值操作，
# 这时候要注意，这个时候赋值操作的右边是没有值的（因为刚才那个是return出去了，并没有给赋值操作的左边传参数），
# 所以这个时候res赋值是None,所以接着下面的输出就是res:None,
# 2.程序会继续在while里执行，又一次碰到yield,这个时候同样return 出4，然后程序停止，print函数输出的4就是这次return出的4
print(next(g))
print('_' * 20)
print(next(g))


