# 作用：和__str__类似，都是定制化输出类得解释，但是__repr__不需要调用，创建了类的对象可以直接输出
# (1) __repr__的目标是准确性，或者说，__repr__的结果是让解释器用的。
# (2)__str__的目标是可读性，或者说，__str__的结果是让人看的。

class A:

    # def __str__(self):
    #     print('this is str')

    def __repr__(self):
        return 'this is repr'


if __name__ == '__main__':
    a = A()
    # print(a.__str__())
    print(a)
