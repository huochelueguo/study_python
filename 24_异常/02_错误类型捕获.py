# 在程序执行时，可能会遇到不同种类的异常，并且需要针对不同类型的异常，做出不同的相应，此时就需要捕获错误类型了
# 在执行代码时，报错的最后一行第一个单词，就是错误类型


# 例子：提示用户输入一个整数，使用8除用户输入的整数并且输出值
try:
    num = int(input('请输入一个整数：'))
    num2 = 8 / num
    print(num2)
except ValueError:
    print('请输入整数，目前输入错误')
except ZeroDivisionError:
    print('除数不能为0')


