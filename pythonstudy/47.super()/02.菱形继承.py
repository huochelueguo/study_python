# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02.菱形继承.py
@Time:NAME.py@Time:2021/1/25 20:36
"""
"""
菱形继承和MRO
    
    A
  /  \
 /    \
B      C
 \    /
  \  /
   D
    菱形继承：
        如上图，C和B继承于A ,D又继承于B和C，按照python3的广度优先原则，先调用父类BC再调用BC父类A
"""


class A(object):

    def __init__(self):
        print('enter a')
        print(self)
        print('leave a')


class B(A):

    def __init__(self):
        print('enter b')
        super().__init__()
        print(self)
        print('leave b')


class C(A):

    def __init__(self):
        print('enter C')
        super().__init__()
        print(self)
        print('leave C')


class D(B, C):

    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')


if __name__ == '__main__':
    """执行顺序根据类.__mro__结果，D-B-C-A-C-B，self都是D自己
    1.创建 D 类的对象 d 时，自动调用 D 类的初始化方法 __init()__，此时的 self 指向 D 类创建的实例对象 d；
    2.调用原则：D->B->C->A->C->B->D
    3.在调用到 B 时，首先输出 “Enter B”，但是运行到父类 A 的初始化方法时不立即调用，反而时转向广度优先级高的 C 类，因为 A 类对于 B 类来说是深度遍历。""""""
    """
    print(D.__mro__)
    d = D()
