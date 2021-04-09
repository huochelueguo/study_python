# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:09.函数传参的2种方式.py
@Time:NAME.py@Time:2021/4/9 17:34
"""
"""
python中函数传参的2种方式：
1.在函数中定义形参
2.使用闭包，在外部函数中传入
"""

# 第一种方法：直接传参


def test(a, b=5):
    print(a+b)


test(4)


# 第二个方法：通过闭包传参
def outer(c):
    # a=5
    def test2(a, b):
        return a * b * c
    return test2


f = outer(3)    # 将test2()的内存地址赋值给f
print(f(2, 5))  # 执行f(a,b)相当于执行了test2(a,b)
