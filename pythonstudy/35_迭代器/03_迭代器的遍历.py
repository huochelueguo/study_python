# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03_迭代器的遍历.py
@Time:NAME.py@Time:2020/8/8 18:46
"""

list = [1, 2, 3, 4, 5]
iter_list = iter(list)

# 方法1：使用next()如果超出越界，将会报StopIteration
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print('- ' * 30)

# 方法2：使用for + next
iter_list = iter(list)
for i in range(13):
    try:
        print(next(iter_list))
    except StopIteration:
        break
print('- ' * 30)

# 方法3： 使用for
iter_list = iter(list)
for i in iter_list:
    print(i)
