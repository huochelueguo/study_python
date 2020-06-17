# 函数中的return可以返回多个值，可以使用元组，
def one(a, b):
    """
    函数返回多个返回值，可以使用元组来承接
    :return: 返回值使用为元组，外部括号也可以省略
    """
    sum = a + b
    c = 'abc'
    # return (sum, c)
    return sum, c


# 使用元组承接返回值
tuple1 = one(40, 60)
print(f'函数返回值类型为元组，值为： {tuple1}')
