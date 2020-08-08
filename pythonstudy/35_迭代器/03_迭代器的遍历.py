# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03_迭代器的遍历.py
@Time:NAME.py@Time:2020/8/8 18:46
"""
# 遍历迭代器使用next()，如果超出越界，将会报StopIteration
list = [1, 2, 3, 4, 5]
it = iter(list)
# for i in range(10):
#     print(next(it)) # 由于循环越界，所以报错StopIteration

# 使用异常捕捉
try:
    while True:
        print(next(it))

except StopIteration:
    exit()

