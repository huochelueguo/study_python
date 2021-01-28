# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03_列表元素相加.py
@Time:NAME.py@Time:2021/1/28 20:47
"""
from functools import reduce

"""
# 请写一个函数，该函数 参数为数字列表，请算出另外一个列表，里面每个元素依次是参数列表里面元素的累计和。
# 比如 参数为[1, 2, 3, 4]
# 结果计算方法为[1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]
# 返回结果就应该是[1, 3, 6, 10]
"""

# 方法1：使用双层循环
l1 = [1, 2, 3, 41]
l2 = []
for i in range(len(l1)):
    num = 0
    for j in range(i+1):
        num += l1[j]
    l2.append(num)
print(l2)


# 方法2：使用reduce
l3 = []
for i in range(1, len(l1)+1):
    l3.append(reduce(lambda x, y: x+y, l1[0:i]))
print(l3)

# 方法3：
l4 = []
sum = 0
for i in range(len(l1)):
    sum += l1[i]
    l4.append(sum)
print(l4)
