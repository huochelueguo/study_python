# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:10_random模块.py
@Time:NAME.py@Time:2020/8/7 18:16
"""
import random
# 常用函数：
# random.random:随机输出[0,1)之间的数
a = random.random()
print(a)

# random.uniform(a, b) — 生成一个范围为 a≤N≤b 的随机数，随机数类型是浮点数；
b = random.uniform(1, 20)
print(b)

# random.randint(a, b) — 生成一个范围为 a≤N≤b 的随机数，随机数的类型是整形，注意与random.uniform(a, b)区别
c = random.randint(1, 20000)
print(c)

# random.randrange(start, stop, step) — 返回从 start 开始到 stop 结束、步长为 step 的随机数(可以用该方法返回随机偶数或者奇数)，示例:
d = random.randrange(0, 100, 5)
print(d)
# 返回随机偶数
e = random.randrange(0, 100, 2)
print(e)
# 返回随机奇数
f = random.randrange(1, 100, 2)
print(f)

# random.sample(seq, k) — 从 seq 序列中随机抽取 k 个独立的元素。
li1 = [1, 2, 3, 4, 5, 6, 7]
print(random.sample(li1, 2))

# random.choice(seq) — 从 seq 序列中随机抽取一个元素，如果 seq 为空，则引发 IndexError 异常。
li2 = []
print(random.choice(li2))   # IndexError: Cannot choose from an empty sequence