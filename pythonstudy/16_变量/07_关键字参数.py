# 关键字参数是一个由键值对组成的集合，允许通过变量名进行匹配，而不是位置。


def dict1(**kwargs):

    a = {**kwargs}
    print(f'输入内容为字典，内容为：{a}')


if __name__ == '__main__':
    # 函数参数为**keargs,传入参数为字典值，为空也可以
    dict1(a=1, b=2, c=3)
    dict1(q=1,)
    dict1()
