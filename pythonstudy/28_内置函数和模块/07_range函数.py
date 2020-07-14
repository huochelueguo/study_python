# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:07_range函数.py
@Time:NAME.py@Time:2020/7/14 上午9:00
"""
# python range函数可创建一个整数列表，一般用在 for 循环中，语法如下：
# range(start, stop, step) //左开右闭区间：  start <= value < stop
# 参数说明：
# start: 计数从 start 开始，默认是从0开始，例如：range（5）等价于range（0， 5）；
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0,5） 是[0,1,2,3,4]没有5；
# step：步长，默认为1
a = range(2, 5)
print(list(a))
b = range(0, 10, 3)
print(list(b))

# for循环中，由于start和step默认都是0，因此一般情况下for循环中，range的值一般都是stop的值
x = 'www.shuopython.com'
for i in range(len(x)):
    print(x[i], end=' ')
print('')


for m in range(2, 17, 4):
    print(x[m], end='/')
