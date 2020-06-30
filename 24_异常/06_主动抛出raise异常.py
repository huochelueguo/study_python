# Exception类：
# 在开发时，如果满足特定的业务需求是，希望抛异常，可以：
#     1.创建一个Exceptinon类的对象
#     2.使用raise关键字抛出异常对象

# 应用场景：
# --在开发中，除了代码执行出错，Python解释器会抛出异常之外
# --还可以根据应用程序特有的业务需求主动抛出异常


# 例子:提示用户输入密码，当输入小于8位时，抛出异常


def input_pwd():
    # 提示用户输入密码
    pwd = input('请输入密码')
    # 判断密码长度
    if len(pwd) >= 8:
        return pwd
    # 如果小于8，抛出异常
    # 1> 创建异常对象，可以使用错误信息字符串作为参数，在外部可以直接输出该字符串
    ex = Exception('密码输入位数不够')
    # 2> 抛出异常对象
    raise ex


try:
    pwd2 = input_pwd()
    print(f'输入的密码为： {pwd2}')
# 使用未知类型错误捕获函数中抛出的异常
except Exception as result:
    print(result)
