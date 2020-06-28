# 多态的概念
# --不同的子类对象调用相同的父类方法，产生不同的执行效果
# ----多态可以增加代码灵活度
# ----以继承和重写父类方法为前提
# ----是调用方法的技巧，不会影响到类的内部设计


class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print(f'{self.name}愉快的玩耍')


class XiaoTianQuan(Dog):

    def game(self):
        print(f'{self.name}在天上玩耍')


class Person(object):
    def __init__(self, name):
        self.name = name

    def play(self, dog):
        print(f'{self.name}和{dog.name}')
    # 让狗玩耍,调用方法一定要有括号
        dog.game()


# 1.创建一个狗对象，传入不同的狗对象实参，会产生不同的执行效果
# wangcai = Dog('旺财')
wangcai = XiaoTianQuan('哮天犬')
# 2.创建一个小明对象
xiaoming = Person('小明')
# 3.让小明调用和狗狗玩的方法
xiaoming.play(wangcai)
