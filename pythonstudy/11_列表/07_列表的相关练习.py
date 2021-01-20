# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:07_列表的相关练习.py
@Time:NAME.py@Time:2021/1/15 20:25
"""
l1 = [1, 2, 4, 5, 15, 21, 12, 423, 54, 115]
l2 = ['2', '3', '21', '13', '22', '32']
"""
 两个列表合并
"""
# 方法1：
print(l1 + l2)
# 方法2：
l1 = [1, 2, 4, 5, 15, 21, 12, 423, 54, 115]
for i in l2:
    l1.append(i)
print(l1)
# 方法3：
l1 = [1, 2, 4, 5, 15, 21, 12, 423, 54, 115]
l1.extend(l2)
print(l1)

"""
将'abcd'添加到l1中，不适用for循环，一句话写出
"""
l1 = [1, 2, 4, 5, 15, 21, 12, 423, 54, 115]
l1.extend([x for x in 'abcd'])
print(l1)

"""
删除列表中的21
"""
l1.remove(21)
print(l1)

"""
删除[1,4]位
"""
del l1[1:4]
print(l1)

"""
将aa替换成大写AA
"""
l1 = [1, 2, 4, 5, 15, 21, 12, 423, 54, 115, 'aa']
l1[-1] = l1[-1].upper()
print(l1)

"""
打印出列表索引
"""
for k, v in enumerate(l1):
    print(k)

"""
输出10-100，倒叙将偶数放入一个新列表中，在筛选出能被4整除的数
"""
l1 = []
for i in range(10, 101):
    if i % 2 == 0:
        l1.append(i)
        l1.sort(reverse=True)
        print(l1)
l1 = [x for x in l1 if x % 4 == 0]
print(l1)
print('-' * 50)

"""
输入内容，将内容插入到一个列表中，如果输入内容与列表中内容重复，则用对应长度*代替
"""
# l1 = ['aaa', 'bb', 'c']
# l2 = []
# while True:
#     str = input('请输入：')
#     if str in l1:
#         l2.append(str.replace(str, '*' * len(str)))
#     else:
#         l2.append(str)
#     print(l2)
# print('-' * 50)
"""
循环打印以下列表每个元素，同时将字母全部改为小写，遇到列表继续循环打印
"""
l1 = [1, 2, 3, 'A', 'Abc', [1, 'a', 'A', 'DS', 44], (5, 3)]
for i in l1:
    if isinstance(i, int):
        print(i)
    elif isinstance(i, str):
        print(i.lower())
    elif isinstance(i, list):
        for j in i:
            if isinstance(j, int):
                print(j)
            elif isinstance(j, str):
                print(j.lower())
            else:
                print(j)
    else:
        print(i)