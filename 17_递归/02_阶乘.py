

def fn(a):
    if a == 1:
        return a
    m = a * fn(a-1)
    return m


b = fn(5)
print(f'5阶乘运算结果是:{b}')
