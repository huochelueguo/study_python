# dir的作用：
# 使用该函数，可以查看到针对该对象的所有属性和方法


# 动物类
class Animal():

    # 类中的2个方法
    def eat(self):
        print(f'eat')

    def sleep(self):
        print(f'sleep')


dog = Animal()
print(dir(dog))
# 输出值为['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'eat', 'sleep']
