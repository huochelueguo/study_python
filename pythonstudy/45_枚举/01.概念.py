# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01.概念.py
@Time:2021/5/21 上午9:01
"""
"""
枚举的概念Enum：
    通常都使用大写字母或者字典来定义常量，但是经常出现常量定义重复或者被修改的问题，因此可以使用枚举类来定义常量
枚举的写法：
    1.引入enum库 from enum import Enum
    2.定义枚举类
    3.定义常量，建议大写
枚举的取值：
    1.名称属性： 类名.常量名.name
    2.对应常量值： 类名.常量名.value
    
"""

from enum import Enum


class Color(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3
    GREEN = 4
    WHITE = 4


print(Color.BLUE.value)  # 获取枚举对应的值
print(Color.GREEN.name)  # 获取枚举定义名
print(Color.WHITE.name)
print(Color.WHITE.value)
print(Color.GREEN.value)