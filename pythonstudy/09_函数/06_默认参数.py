# 调用函数时，如果默认参数的值没有传入，则直接使用默认值


def info(name, age=20):
    print(f'name = {name}')
    print(f'age = {age}')
    return


# 有默认参数，不输入年龄，使用默认值
info('小明')
info('张三', 50)
