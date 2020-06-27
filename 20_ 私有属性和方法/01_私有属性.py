# 应用场景：
# --在实际开发中，对象的某些属性可能只希望在 对象的内部使用，而 不希望在外部访问
# --私有属性 就是对象不希望公开的属性
# --私有方法 就是对象不希望公开的方法
#
# 定义方式：
# 在定义私有属性或方式时，在属性名或者方法名前 增加 两个下划线，即为私有


class Human(object):
    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __age(self):
        # 在对象的方法内部，是可以访问对象的私有属性
        print(f'{self.name}的年龄是{self.__age}')


fangfang = Human('小芳')
print(f'{fangfang.name}')
# 外部无法直接访问对象的私有属性
# fangfang.__age
# 外部无法直接访问对象的私有方法
# fangfang.__age

