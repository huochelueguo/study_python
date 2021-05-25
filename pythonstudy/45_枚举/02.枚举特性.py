# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02.枚举特性.py
@Time:2021/5/25 上午9:13
"""
"""
枚举特性：
    1.枚举类中定义的值，外部不允许修改
    2.枚举类中，常量值允许重复，出现重复时，后面出现的名称变为别名
    3.枚举类中，常量名称不允许重复
    4.如果想让枚举类中值也不重复，可以引入unique
    5.可以使用for循环遍历枚举，但是不会将别名输出
    6.遍历枚举不会把别名给循环处理，要把别名也遍历出来就用枚举类的__menbers__属性
"""
from enum import Enum,unique


# @unique
class Color(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3
    GREEN = 4
    WHITE = 4
    # WHITE = 56


print(Color.WHITE.value)    # 存在两个WHITE，不允许重复因此会报错
print(Color.WHITE.name)     # 因为加了unique，因此枚举值也不允许一样；如果没加@unique，该句输出为GREEN
for i in Color:
    print(i, i.value, i.name)   # 输出结果缺少WHITE

for j in Color.__members__:
    print(j)