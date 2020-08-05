# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_赋值.py
@Time:NAME.py@Time:2020/8/5 上午8:44
"""
# 简单数据（不可变数据）的赋值,一个变量改变时，另一个变量值不会改变（包括值和内存地址）
a = 11
b = a
print(a, id(a))
print(b, id(b))
# 11 4430609376
# 11 4430609376
print('* *' * 20)
a = 12
print(a, id(a))
print(b, id(b))
# 12 4430609408
# 11 4430609376
print('* *' * 20)
b = 5
print(a, id(a))
print(b, id(b))
# 12 4430609408
# 5 4430609184
print('* *' * 20)

# 复杂数据（可变数据）的赋值，一个变量改变时，与其相关的值都会改变
m = [1, 2, 3]
n = m
print(m, id(m))
print(n, id(n))
# [1, 2, 3] 4438771968
# [1, 2, 3] 4438771968
print('* *' * 20)
m[0] = 11
print(m, id(m))
print(n, id(n))
# [11, 2, 3] 4438771968
# [11, 2, 3] 4438771968
print('* *' * 20)
n[0] = 12
print(m, id(m))
print(n, id(n))
# [12, 2, 3] 4580137152
# [12, 2, 3] 4580137152

