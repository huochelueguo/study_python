# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:08.字典转换与区直.py
@Time:2021/4/25 上午9:21
"""
"""
转换：任何类型都可以转化成字典
"""



"""
取值：可以分别取出字典的key或者value，输出结果需要强转为list
"""
dict1 = {
    "name": 222,
    "age": 20,
    "sex": 0,
    "weight": 75
}
print(list(dict1.keys()))
print(list(dict1.values()))