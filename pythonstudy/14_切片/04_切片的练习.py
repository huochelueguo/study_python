# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:04_切片的练习.py
@Time:2021/1/20 上午9:21
"""

"""
练习1： 对如下列表进行修改
"""
l1 = [1, 3, 4, 5, 'aa', 8, 'd', 'c']
# 取出前三个值
print(l1[0:3])
# 取出[3,5,8]
print(l1[1:6:2])
# 取出['c']
print(l1[-1])
print(l1[7])
# 取出[4,3,1]
print(l1[0:3:-1])   # 输出为空，顺序和起始点不一致
print(l1[-6::-1])