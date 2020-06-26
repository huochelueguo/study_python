# 重写（override）
# 当父类的方法不能满足子类的需求时，可以对其方法重写
# 重写父类的2种情况：
# 1. 覆盖父类的方法
# 2. 对父类方法进行扩展

# 覆盖父类的方法
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

    # 对run这个类进行重写，修改这个方法
    def run(self):
        print(f'{self.name}的腿太短了，跑起来真慢')


# 子类创建一个队形
keji = Keji('小柯基')
print(keji)
keji.eat()
keji.bark()
keji.short_leg()
# 由于子类修改了父类的方法，因此子类这时候调用重写后的方法
keji.run()
print('_' * 50)
# 父类创建一个对象，不同的对象调用对应类中的方法
dog = Dog('旺财')
dog.run()
