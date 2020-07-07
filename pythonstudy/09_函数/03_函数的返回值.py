#返回值使用return关键字


def fanhui(num1):
    """判断输入的值和50的大小"""

    if num1 > 50 :
        return "数字很大"
    else:
        return "数字很小"
    print("return关键字后面代码不会被执行")


print(fanhui(5))
