# Python 中，么有真正意义上的私有
# --正常开发中，不允许使用这个方法去访问私有内容
# --再给属性 方法命名是，实际上是对名称做了特殊的处理，使得外界无法访问到
# --处理方式，在名称前面加上 _类名  ： _类名__名称



class Human(object):
    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secert(self):
        # 在对象的方法内部，是可以访问对象的私有属性
        print(f'{self.name}的年龄是{self.__age}')


fangfang = Human('小芳')
print(f'{fangfang.name}')
# 外部通过_类名__名称获取私有属性
print(f'通过_类名__私有名称的方法就能够访问到私有内容，私有内容的值是：{fangfang._Human__age}')
# 外部通过_类名__名称获取私有方法
fangfang._Human__secert()
