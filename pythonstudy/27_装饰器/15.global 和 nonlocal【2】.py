# a = 5


def outter():
    a = 10

    def inner():
        print(a)
        print(f'如果没有声明任何内容，则按照就近原则查找上一层，因此a为:10')
        return a

    return inner


def outter2():
    a = 10

    def inner2():
        nonlocal a  # nonlocal仅修改调用处后的值，不修改原值
        a = 20
        print(a)
        print(f'因为声明了nonlocal，因此将会改变局部的a，此处输出a为20')

    print(f'外部的a值不变还是10:{a}')
    return inner2


def outter3():
    a = 10

    def inner3():
        global a  #
        a = 30
        print(a)
        print(f'因为声明了global，因此将会改变全局的a，此处输出a为30')

    print(f'外部的a值也将改为30:{a}')
    return inner3


o = outter()
o()
print('-' * 50)
o2 = outter2()
o2()
print('-' * 50)
o3 = outter3()
o3()
