# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:11_random模块02.py
@Time:NAME.py@Time:2020/8/7 18:45
"""
# 使用random模块实现简单的验证码功能。要求每次随机输出四位数字
import random
li1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
li2 = []
for i in range(4):
    i = random.choice(li1)  # 使用random的choice方法，随机从li1数组中抽取一个
    li2.append(i)
print(li2)

for m in li2:   # 将列表格式的四位随机数，遍历输出得方法转换为数字，由于序列中元素不是字符串，因此不可以使用join方法
    print(m, end=' ')
print()
print(type(m))
