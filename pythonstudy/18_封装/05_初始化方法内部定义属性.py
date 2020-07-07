# 在创建对象的同时，就设置对象的属性，可以修改__int__方法：
# 1. 将希望设置的属性作为参数，定义为__init__方法的参数
# 2. 在方法的内部使用self.属性 = 形参 的方法接收外部传入的参数
# 3. 创建对象时，使用 对象 = 类名（实参1，实参2。。。）的方式调用


class Animal:

    # 方法加形参，接收传入的实参
    def __init__(self, name, age):
        # self.属性名 = 属性的初始值
        self.name = name
        print(f'小动物名字是{self.name}')
        self.age = age
        print(f'{self.name}的年龄是{self.age}')

    def eat(self):
        if self.name == '旺财':
            print(f'{self.name}爱吃肉')
        if self.name == '咪咪':
            print(f'{self.name}爱吃鱼')
        else:
            pass


# 将狗的名字实参 传入
dog = Animal('旺财', 5)
dog.eat()

print('-'*50)
# 定义另一个对象小猫
cat = Animal('咪咪', 3)
cat.eat()

