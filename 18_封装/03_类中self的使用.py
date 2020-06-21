# 在类中，使用self的作用
# 可以用过self. 的来访问对象的属性
# 可以通过self. 的来访问对象的其他方法


class Animal:

    def eat(self):
        # 访问属性
        print('%s爱吃肉肉' % self.name)

    def sleep(self):
        print(f'{self.name}睡觉打呼噜')

    def run(self):
        # 访问其他方法
        dog.eat()
        print('吃完之后就四处乱跑')


dog = Animal()
dog.name = '多多'
print(f'狗狗的名字是{dog.name}')
dog.sleep()
dog.eat()
dog.run()
