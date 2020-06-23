# 练习1：
# 小明体重75公斤
# 小明每次跑步会减肥0.5公斤
# 小明每次吃零食会增肥1公斤

class Person(object):

    # 初始化方法，将实参传入
    # self.属性名 = 实参值
    def __init__(self, name, weight):
        self.name = name
        self.wight = weight

    def __str__(self):
        # 必须要有返回值，且返回值必须是字符串
        return f'小朋友的名字是{self.name},体重是{self.wight}'

    def run(self):
        self.wight -= 0.5
        print(f'{self.name}每次跑步会减肥,跑步后体重为{self.wight}')

    def eat(self):
        self.wight += 1
        print(f'{self.name}每次吃零食会增肥，吃完体重为{self.wight}')


# Person类创建对象，并且对初始化值进行赋值，将实参传入
xiaoming = Person('小明', 75.0)
print(xiaoming)
xiaoming.run()
xiaoming.eat()

print('-'*20)

xiaomei = Person('小美', 45)
print(xiaomei)
xiaomei.run()
xiaomei.eat()
