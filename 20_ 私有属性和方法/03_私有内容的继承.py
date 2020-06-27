# --子类对象中，不能直接访问父类对象中的私有属性或方法
# --子类对象可以通过 父类中的共有方法 间接的访问到私有属性或私有方法
# ---私有属性、方法：对象的隐私，不对外公开，外界和子类都不能直接访问
# ---私有属性、方法通常做一些内部的事情



class Human(object):
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secert(self):
        print(f'这个是私有方法，子类没有方法直接访问哦')

    # 通过公有类调用私有方法和属性
    def public(self):
        print(f'通过公有方法，可以访问到类内部的私有方法和属性')
        print(f'私有属性年龄的值为{self.__age}')
        print(f'下面调用私有方法：__Secert')
        self.__secert()


class Woman(Human):
    # 扩展父类的方法
    def __init__(self, name, fruit):

        self.name = name
        self.fruit = fruit
        # 通过super().方法名 来调用原父类的方法，原父类方法需要一个参数，这里传入
        super().__init__(name)

    def favorite(self):

        print(f'{self.name}最喜欢吃的东西是{self.fruit}')


# 父类对象，也无法直接访问父类中的私有方法和属性
# xiaofang = Human('小芳')
# # xiaofang.__secert
# xiaofang.public()

xiaoli = Woman('小丽', '西瓜')
# 子类通过父类的公有方法访问类的私有属性和方法,无法直接调用父类私有内容
# xiaoli.__secert
xiaoli.public()
# 子类单独的方法
xiaoli.favorite()
