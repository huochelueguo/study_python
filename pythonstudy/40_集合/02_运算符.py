# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_运算符.py
@Time:2021/4/27 上午9:29
"""
"""
集合的主要作用：求两个集合的相互关系，结果还是一个集合
    1. 交集： &
    2. 并集 |
    3. 差集 -
    4. 对称差集【两个集合独有的集合】 ^
    5. 父子集【是否为包含关系，返回bool】 >
"""

set1 = {4, 5, 6, 7, 8, 9}
set2 = {1, 2, 3, 4, 5, 6}
set3 = {1, 2}

print(f'集合的交集为{set1 & set2}')
print(f'集合的并集为{set1 | set2}')
print(f'set1为基准，集合的差集为{set1 - set2}')   # set1中有，但是set2里面没有的数据集合
print(f'set2为基准，集合的差集为{set2 - set1}')
print(f'对称差集，即两个集合出去并集以外的内容为{set1 ^ set2}')
print(f'set1为基准，父子集为{set1 > set3}')  # false
print(f'set2为基准，父子集为{set2 > set3}')  # true
