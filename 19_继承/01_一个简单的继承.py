# 继承的语法:
# class 子类（父类名）：
#     pass

# 继承的特点
# 子类继承自父类，可以直接使用父类已经封装好的方法，不需要再次开发
# 子类中应该还有自己特有的属性和方法

# 继承的说法：
# 1.子类和父类
# 2.派生类和基类


# 动物类为父类,无指定父类是，建议继承于基类object
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


# 创建一个狗类，由于狗类是动物类的子类，因此可以直接调用父类的方法和属性
dog1 = Dog('妞妞')
# print(dog1)
print(f'狗狗的名字是{dog1.name}')
# 父类的方法
dog1.eat()
dog1.run()
# 子类的方法
dog1.bark()
