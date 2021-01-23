# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_简单的用法.py
@Time:NAME.py@Time:2021/1/23 18:43
"""

"""
super() 作用：
    当子类具有和父类同名的方法时，子类执行该方法将仅执行子类方法中的内容，如果同时想调用父类方法中的内容，就可以使用super().来调用
"""

class Human():

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def paly(self):
        print('打麻将')


class Man(Human):

    def __init__(self, skill, age, name):
        super().__init__(age, name)
        self.skill = skill

    def paly(self):
        super().paly()
        print(self.skill)

man = Man(skill='抽烟', age=20, name='q')
man.paly()