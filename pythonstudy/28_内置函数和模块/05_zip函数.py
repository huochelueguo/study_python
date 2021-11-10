# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:05_zip函数.py
@Time:NAME.py@Time:2020/7/13 下午9:11
"""
# 对多个有序数据按照顺序取值，形成新的数据组，可以强转为list
# 如果两个迭代器的长度不同，自动根据最短的迭代器长度匹配！
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 0]

zip_data = zip(a, b, c)
print(type(zip_data))
list_zip = list(zip_data)
print(list_zip)
# 输出：[(1, 5, 9), (2, 6, 10), (3, 7, 0)]

# 对于单一数组里面嵌套其他数据类型如字符串的，也可以进行zip压缩,使用*xx
strs = ["flower","flow","flight"]
for i in zip(*strs):
    print(i)