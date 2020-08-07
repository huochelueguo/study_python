# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03_filter.py
@Time:NAME.py@Time:2020/8/7 上午9:09
"""
# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# 注意：Python3 返回的结果为迭代器，需要强转为list

# 练习：输出100以内的质数
li = []
for i in range(1,101):
    li.append(i)
print(li)


def zhishu(x):
    for m in range(2, x):
        if x % m == 0:
            break
        else:
            return x


data = filter(zhishu, li)
print(list(data))

