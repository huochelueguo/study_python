# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:04_迭代器和for.py
@Time:NAME.py@Time:2021/3/24 14:31
"""

"""
for循环工作原理：
    1.iter(x) 得到一个迭代器
    2.每次循环相当于调用了next(x)，取出一个值
    3.循环执行2，直到stopIteration时，for循环会将捕捉到异常，并且结束循环
"""
dic1 = {'a': 1, "b": 2, "c": 3, "d": 4}
for k in dic1:
    print(k)

for k, v in dic1.items():
    print(f'{k}:{v}')