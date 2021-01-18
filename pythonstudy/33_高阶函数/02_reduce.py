# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_reduce.py
@Time:NAME.py@Time:2020/8/6 20:53
"""
# reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 注意：python3后，reduce()函数需要导入包后才可以使用
from functools import reduce

li1 = [1, 2, 3, 4, 5]


def add(a, b):
    return a + b


num = reduce(add, li1)
print(num)


# 练习：输出阶乘
li2 = []
for i in range(1, 101):
    li2.append(i)
print(li2)


def cheng(a, b):
    return a * b


sum2 = reduce(cheng, li2)
print(sum2)


# 给出一个数组，输出他的数字，比如[1,2,3]输出123
li = [1, 2, 3]

# 方法1：
str1 = ''
for i in li:
    str1 += str(i)
print(int(str1), type(int(str1)))

# 方法2：
def func(x, y):
    return x * 10 + y
print(reduce(func, li), type(reduce(func, li)))

# 方法3：
print(reduce(lambda x, y: x*10+y, li))

# 将str转换成为int，不使用int()强转
dict = {}
str = '12346'
for i in range(0, 11):
    dict[str(i)] = i
print(dict)
for i in range(str):
    https: // www.liaoxuefeng.com / wiki / 1016959663602400 / 1017329367486080