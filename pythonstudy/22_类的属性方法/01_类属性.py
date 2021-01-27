class A(object):

    a = 0   # 公有类属性
    _b = 0  # 私有类属性

    def __init__(self, num):
        self.num = num

    def count_num(self):
        A.a += 1    # 类属性只能通过类或者类的实例来调用
        A._b += 1
        return A.a, A._b

    def siyou(self):
        return A._b * 10


for i in range(10):
    a = A(i).count_num()
    print(a)
b = A(2)
print(b.siyou())    # 通过类的方法间接调用类的私有属性
print(b.a)
