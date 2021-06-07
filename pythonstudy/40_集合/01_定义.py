# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_定义.py
@Time:2021/4/27 上午9:22
"""
"""
在{}使用逗号分隔的多个元素，多个元素必须满足以下条件：
    1.元素必须为不可变类型()
    2.集合内元素无序
    3.集合内元素不允许重复
"""
s = {1, 2, 3}
print(set(s))
print('_' * 20)

# s = {1, 2, [3, 3, 3]}
# print(set(s))   # 因为列表为可变元素，因此无法强转成集合

s1 = {1, 2, 3, 4, 5, 'ddd', 6, 7, 8, 'a', 'b'}
print(s1)   # 无序 {1, 2, 3, 4, 5, 6, 7, 8, 'a', 'ddd', 'b'}
print('_' * 20)
