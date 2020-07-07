# 用途：开发是，如果想使用print输出对象变量时，能够打印自定义的内容，就可以用该方法
# 使用中注意事项：必须要有返回值，且必须是字符串
# 如果不使用__str__，print对象变量输出的为该对象创建时分配的内存地址，具体见01_类


class Animal:

    def __init__(self, name):
        # 初始化变量传入的实参，要使用形参去接，否则无法生效
        # self.属性名 = 属性的初始值
        self.name = name
        print(f'狗的名称为{self.name}')

    def __del__(self):
        print('这个是对象被销毁前最后执行的方法')

    def __str__(self):
        return '定制变量输出的内容为，我是%s' % self.name


dog = Animal('小花')
print(dog)
print('-'*50)


