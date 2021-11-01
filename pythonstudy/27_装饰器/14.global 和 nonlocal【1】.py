a = 5
print(f'未修改前a为：{a}')    # 未修改前a为：5


def sum():
    global a
    a = 50
    return a


print(sum())
print(f'修改后的a为：{a}')    # 修改后的a为：50


def sum2():
    return a * a


print(f'修改后，函数调用时，也是修改后的值:{sum2()}')    # 2500
