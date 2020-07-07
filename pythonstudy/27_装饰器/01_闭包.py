# 闭包：在函数中再嵌套一个函数，并且引用外部函数的变量，这就是一个闭包了


def outer(x):
    print(f'x = {x}')

    def inner(y):
        print(f'y = {y}')
        return x + y

    return inner


print(outer(5)(9))
