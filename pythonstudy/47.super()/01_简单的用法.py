# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_简单的用法.py
@Time:NAME.py@Time:2021/1/23 18:43
"""

"""
super() 
https://blog.csdn.net/dxk_093812/article/details/87553937
作用：
    当子类具有和父类同名的方法时，子类执行该方法将仅执行子类方法中的内容，如果同时想调用父类方法中的内容，就可以使用super().来调用
写法：
    super(type[, object-or-type])
        type -- 类。
        object-or-type -- 类，一般是 self
        Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :
使用方法：
    1、构造方法中，有同名参数可以使用super().__init__(参数)
    2、普通方法中，使用super().xx()调用父类中的xx方法   
"""


class Human():

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def paly(self):
        print('打麻将')


class Man(Human):

    def __init__(self, skill, age, name):
        super().__init__(age, name) # 调用父类init中的age和name
        self.skill = skill

    def paly(self):
        super().paly()  # 调用父类的play方法
        print(f'技能是{self.skill},年龄是{self.age},姓名为{self.name}')


class Women(Human):

    def __init__(self, skill, age, name):
        super().__init__(age, name)
        self.name = name * 10   # 自己的类中进行初始化数据，因此name和age值和父类中不一致
        self.age = age - 1
        self.skill = skill

    def paly(self):
        print(f'技能是{self.skill},年龄是{self.age},姓名为{self.name}')


if __name__ == '__main__':
    man = Man(skill='抽烟', age=50, name='q')
    man.paly()
    women = Women(skill='KTV', age=100, name='q')
    women.paly()