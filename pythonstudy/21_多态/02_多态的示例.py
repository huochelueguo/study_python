# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_多态的示例.py
@Time:2021/1/21 下午11:05
"""

# 三个军种都继承自士兵类，但是每个军种的攻击和撤退方法都不一样
class Soldier():

    def attack(self):
        print('发出出击')

    def back(self):
        print('回撤！')


class Navy(Soldier):

    def attack(self):
        super().attack()
        print('海军出击')

    def back(self):
        super().back()
        print('海军撤退')


class AirForce(Soldier):

    def attack(self):
        super()
        print('空军出击')

    def back(self):
        super()
        print('空军撤退')


class Army(Soldier):

    def attack(self):
        print('陆军出击')

    def back(self):
        print('陆军撤退')


obj1 = Navy()
obj2 = AirForce()
obj3 = Army()
li = [obj1, obj2, obj3]
print('1、全军出击； 2、全军撤退； 3，空军出击，其他撤退')
str = input('请输入')
for i in li:
    if str == '1':
        i.attack()
    elif str == '2':
        i.back()
    elif str == '3':
        if isinstance(i, AirForce):
            i.attack()
        else:
            i.back()
    else:
        print('无此命令')
        break
