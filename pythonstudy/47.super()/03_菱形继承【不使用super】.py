# 如果在子类中不使用super().func的方法调用父类，多继承可能就会出现重复调用同一个父类得情况

class A(object):

    def __init__(self):
        print('enter a')
        # print(self)
        # print('leave a')


class B(A):

    def __init__(self):
        print('enter B')
        A.__init__(self)
        # print(self)
        # print('leave B')


class C(A):

    def __init__(self):
        print('enter C')
        A.__init__(self)
        # print(self)
        # print('leave C')


class D(B, C):

    def __init__(self):
        print('enter D')
        B()
        # 等同于 B.__init__()
        C()
        # print('leave D')


if __name__ == '__main__':

    print(D.__mro__)
    d = D()
