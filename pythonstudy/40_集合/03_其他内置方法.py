# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03_其他内置方法.py
@Time:2021/4/29 上午9:31
"""
"""
其他需要掌握的内置方法：
    1. 删除discard/remove
    2. 添加 add/update
    3. 是否存在 in/not in
    4. 清空 clear
"""
set2 = {1, 2, 3, 4, 5, 6}

print(set2.discard(22))  # 删除不存在的返回none 不会报错
print(set2)
# print(set2.remove(22))  # 删除不存在的报错

set2.update(['aa', 11, 14, 12,31])    # 将数据拆分后插入集合中
print(set2)

print(5 in set2)

# print(set2.clear())
del set2    # 直接清除了该集合，再次输出报错
# print(set2)