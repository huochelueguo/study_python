# 对父类方法进行扩展
# 如果在开发中，子类的方法实现中包含父类的方法实现
#  父类原本封装的方法实现 是 子类方法的一部分

# 就可以使用 扩展 的方式
# 1. 在子类中重写父类的方法
# 2. 在需要的位置使用 super().父类方法 来调用父类方法的执行
# 3. 代码其他位置针对子类的需求，编写对应的代码实现
#
# super
# - 在Python中 super 是一个特殊的类
# - super() 就是使用super 类创建出来的对象
# - 最常见的使用情况：重写父类方法时，调用父类中的方法实现

# 扩展父类的方法
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
        # 使用super().调用父类，执行父类方法
        super().run()
        # 编写子类自己的剩余代码
        print(f'但是{self.name}的腿太短了，不能上楼')


keji = Keji('小柯基')
print(keji)
keji.eat()
keji.bark()
# 调用子类中跑的方法，该方法继承于父类，类中使用super().调用了父类的方法
keji.run()
