#在一个函数中嵌套调用另一个函数

def hanshu1():
    return ('我是第一个函数')


def hanshu2(a, b):
    print(hanshu1())
    sum = a+b
    return sum


print(hanshu2(3, 5))