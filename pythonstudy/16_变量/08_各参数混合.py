# 参数排序为：位置参数--默认参数--可变参数--关键字参数


def canshu(a, b, c=10, *args, **kwargs):
    print(f'a的值为：{a}')
    print(f'a的类型为：{type(a)}')
    print('_' * 20)
    print(f'b的值为：{b}')
    print(f'b的类型为：{type(b)}')
    print('_' * 20)
    print(f'c的值为：{c}')
    print(f'c的类型为：{type(c)}')
    print('_' * 20)
    list1 = [*args]
    print(f'*args的值为：{list1}')
    print(f'*args类型为:{type(list1)}')
    print('_' * 20)
    dict1 = {**kwargs}
    print(f'**kwargs的值为：{dict1}')
    print(f'**kwargs类型为:{type(dict1)}')


canshu(1, 2, 5, 6, 7, 8, 10, aa=1, bb=2, cc=3)
canshu(1, 2, 'a', 'b', 'c', aa=1, bb=2, cc=3)
