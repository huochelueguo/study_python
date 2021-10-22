# 概念：对于传入的对象，不管是属于谁的，只要对象调用的方法能正常执行，就不报错

class Animal:

    def walk(self):
        print('动物可以跑')

    def eat(self):
        print('动物能吃东西')


class Person:

    def walk(self):
        print('人类可以跑')

    def eat(self):
        print('人类能吃东西')


class Rebot:

    def walk(self):
        print('机器人会走路')


# 该方法不管传入得对象是属于哪个，只要他具有walk和eat方法就不会报错
def func(a):
    a.walk()
    a.eat()


dog = Animal()
func(dog)
man = Person()
func(man)
# rebot1 = Rebot()
# func(rebot1)    # 因为机器人没有walk方法，因此会报错AttributeError: 'Rebot' object has no attribute 'eat'
