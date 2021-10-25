class Animal:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def xingming(self):
        print(f'名称为{self.name}')

    def yanse(self):
        print(f'颜色是{self.color}')


a = Animal('狗子', 2, '黑色')
# 使用hasster来判断，对象是否具有某个方法，返回为波尔值
print(hasattr(a, 'yanse'))
print(hasattr(a, 'anse'))
# 同样，也可以通过hasster来判断对象是否具有某个属性
print(hasattr(a, 'color'))

# 使用getter来获取对象得属性值，当不存在该属性时，将会报错，为防止报错，可以再getter中增加第三个参数
# 也可以将getter获取到得方法赋值给其他变量，执行该方法
print(getattr(a, 'age'))
b = getattr(a, 'yanse')
b()
print(getattr(a, 'age1', 'error'))

# 使用setter来设置对象得属性，将会覆盖之前的值，如下年龄最初未2，下面代码将年龄改为了5
setattr(a, 'age', 5)
print(getattr(a, 'age'))

# 使用delter可以删除对象得属性，不能删除方法
delattr(a, 'age')
# print(a.age)  # AttributeError: 'Animal' object has no attribute 'age'
print(getattr(a, 'age', 'not have'))
