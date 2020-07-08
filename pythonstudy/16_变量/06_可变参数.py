# *args和**args适用于函数的参数不确定的时候。*args可以看做是多个变量组成的list。**args可以看做是个字典
# 可以单独使用，也可以一起使用，但是一起使用时顺序固定不能改变


def add(*args):

    b = 0
    for a in args:
        b += a
    print(f'输入内容求和为:{b}')


def dict1(**kwargs):

    a = {**kwargs}
    print(f'输入内容为字典，内容为：{a}')


if __name__ == '__main__':
    # 函数参数为*args,传入参数为列表值可以多样化，为空也可以，不会报错
    add(4, 6)
    add()
    add(2, 777, 4335345, 2)
    print('_' * 50)
    # 函数参数为**keargs,传入参数为字典值，为空也可以
    dict1(a=1, b=2, c=3)
    dict1(q=1,)
    dict1()


