# 当继承的子类，除了有父类的参数外，自己可能还有一些参数，这时候在初始化时，需要试用super调用父类


class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def father_method(self):
        print('this is father')


class Dog(Animal):
    # 子类有自己得参数时，先调用父类，获取共有参数，之后再写自己得
    def __init__(self, color, name, age):
        super().__init__(name, age)
        self.color = color

    def son_method(self):
        super().father_method()
        print(f'dog is {self.color}')


keji = Dog('黑色', 'wangwang', 2)
keji.son_method()
print(keji.name)
