# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_基本概念.py
@Time:2021/6/16 9:05 上午
"""
"""
反射的概念:
    指在程序运行过程中可以动态的获取对象的信息，（比如事先不知道用户输入的网址，当输入网址后，根据对应地址执行不同操作）
    对于任意一个类，都可以知道这个类的所有属性和方法；
    对于任意一个对象，都能够调用他的任意方法和属性。

为何要用反射：    


反射的实现：
    1、使用dir能够查看所有属性，其返回的值都是字符串格式,使用hasster等来判断时，也就是使用这些字符串代表函数
    2、使用自带的hasattr、getattr、setattr、delattr来判断
"""


class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def man(self):
        print(f'名字是{self.name},年龄是{self.age}')


m = Human('小丽', 20)
print(dir(m))
