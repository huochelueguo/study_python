# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:07.字典的删除2.py
@Time:2021/4/23 上午9:33
"""
"""
字典的删除方法：
    1.del dict[key] 删除某个key,value
    2.del dict 删除整个字典,删除后字典不存在
    3.dict.clear 清空整个字典，返回空字典
    4.dict pop(key) 清空字典某个key,同时使用res可以返回删除元素的value
    5.dict popitem 删除最后一个元素
"""
dict1 = {
    "name": "zhangsan",
    "age": 20,
    "sex": "man",
    "weight": 75
}

del dict1["sex"]    # 删除某个key
print(dict1)

del dict1   # 删除整个字典，因此后面无法使用该字典

dict1 = {
    "name": "zhangsan",
    "age": 20,
    "sex": "man",
    "weight": 75
}

dict1.clear()   # 清空字典
print(dict1)


dict1 = {
    "name": "zhangsan",
    "age": 20,
    "sex": "man",
    "weight": 75,
    '5':22
}
res = dict1.pop('sex')  # 删除某个元素
print(dict1)
print(res)

dict1.popitem() # 删除最后一个元素
print(dict1)