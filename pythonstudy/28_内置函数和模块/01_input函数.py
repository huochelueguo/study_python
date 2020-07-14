# input是Python的内置函数也是交互式函数，获取用户输入内容


while True:
    str1 = input('请输入8位数字：')
    if len(str1) > 8:
        print(f'输入内容过长，请检查')
    elif len(str1) < 8:
        print(f'输入内容过短，请检查')
    else:
        print(f'输入内容为：{str1}')
        break




