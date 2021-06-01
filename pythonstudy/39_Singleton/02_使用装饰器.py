# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_使用装饰器.py
@Time:2021/6/1 9:30 上午
"""
"""
使用装饰器实现单例模式

"""


def singleton(func):
    single = {}   # 存储多个类的实例

    def wrapper(*args, **kwargs):   # 将类传入装饰器，判断装饰器中的字典是否有该类，没有生成一个且返回
        if func not in single:
            single[func] = func(*args, **kwargs)    # func(*args, **kwargs) 表示实现原函数内容，及实现了类的__new__
            print(single)
        return single[func]

    return wrapper


@singleton
class abc:

    def __init__(self):
        pass
        # self.num = num

    # def add(self):
    #     return self.num + 5


s1 = abc()
s2 = abc()
print(s1, s2)
