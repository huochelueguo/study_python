# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:09_斐波那契数列求和(面试题).py
@Time:NAME.py@Time:2021/3/30 16:38
"""
"""
题目：有一个序列：1， 1/2, 2/3, 3/5, 5/8....写一段代码，求出序列前十项和
思路：斐波那契数列求和
"""

"""
方法1：非递归求斐波那契数列
"""
li1 = []
li2 = []
for i in range(21):
    if i == 0 or i == 1:
        li1.append(1)
    else:
        li1.append(li1[i-2] + li1[i-1])
print(li1)
for j in range(int(len(li1)/2)):
    if j == 0 :
        li2.append(1)
    else:
        li2.append(li1[j]/li1[j+1])
print(li2)
print(sum(li2))
print('_' * 100)
"""
方法2：递归求斐波那契数列
"""
li3 = []
li4 = []
def fb(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fb(n-2)+fb(n-1)
for i in range(21):
    li3.append(fb(i))
print(li3)
for j in range(int(len(li3)/2)):
    if j == 0 :
        li4.append(1)
    else:
        li4.append(li3[j]/li3[j+1])
print(li4)
print(sum(li4))
print('_' * 100)
"""
方法3： 使用生成器
"""
li5 = []
def fb(n):
    i = 0
    a = b = 1
    while i <= n:
        yield a
        a, b = b, a+b
g = fb(21)
for j in range(21):
    li5.append(next(g))
print(li5)