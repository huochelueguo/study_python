# 在函数内部，使用方法对可变类型数据进行修改时，会影响到外部的实参


def demo(list1):
    # 使用方法修改可变类型数据，会直接导致该数据外布值一并修改
    list1.append(5)
    return list1


list = [1, 2, 3, 4]
print(f'修改之前的list1为{list}')
print(f'函数输出结果：{demo(list)}')
print(f'由于函数内部使用方法修改，修改之后的list值为{list}')
