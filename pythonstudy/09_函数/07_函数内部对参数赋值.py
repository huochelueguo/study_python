# 无论参数是可变或者不可变，在函数内部对参数赋值不会影响外部实参


def demo(num, list1):
    print('函数内部')
    num += 100
    list1 = [9, 9, 9]
    print(f'函数内部中，num的值为{num}')
    print(f'函数内部中，list1列表的值为{list1}')


gl_num = 50
gl_list = [1, 2, 3, 4]
demo(gl_num,gl_list)
print('函数外部')
print(f'全局变量的值为{gl_num,gl_list}')

