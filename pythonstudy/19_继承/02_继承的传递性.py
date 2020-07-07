# 一个类可以继承父类和父类的父类：
# C类继承自B类，B类继承于A类，那么C类就拥有AB两个类的方法和属性


class Animal(object):

    def __init__(self, name):

        self.name = name

    def __str__(self):
        return f'动物名字是{self.name}'

    def run(self):
        print(f'{self.name}非常爱跑')

    def eat(self):
        print(f'{self.name}非常爱吃')


# 定义一个子类，狗类，狗也属于动物的一种
class Dog(Animal):
    def bark(self):

        # 可以直接调用父类的属性值
        print(f'{self.name}总是汪汪叫')


# 创建一个狗类的子类，柯基类
class Keji(Dog):
    def short_leg(self):
        print(f'{self.name}是柯基，柯基有可爱的小短腿')


kj = Keji('小柯基')
# 调用父类的父类的方法
print(kj)
print(kj.eat())
print(kj.run())
# 调用父类方法
print(kj.bark())
# 调用自己的方法
print(kj.short_leg())
