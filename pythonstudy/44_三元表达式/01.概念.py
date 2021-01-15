# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01.概念.py
@Time:NAME.py@Time:2021/1/15 17:46
"""
"""
写法： 条件为真时的结果 if 判断的条件 else 条件为假时的结果
"""

# 实例：输出[1,100]内能被3整除的数字
li1 = []
li2 = []
for i in range(100):
    li1.append(i) if i % 3 == 0 else li2.append(i)
print(li1)
print(li2)