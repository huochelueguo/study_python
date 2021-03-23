# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:06_排序找到最大出现次数.py
@Time:NAME.py@Time:2021/3/23 16:38
"""

"""
题目：
    python_exercise_给定一个只包含正整数的非空数组,返回该数组中重复次数最多的前N个数字 ,
    返回的结果按重复次数从多到少降序排列(N不存在取值非法的情况)
思路：
    将列表用元组去重后，创建一个字典，将值赋值给列表的KEY，循环遍历原数组，遇到一次+1，最后对字典排序后输出
"""
a = [1, 6, 7, 4, 4, 5, 4]
b = list(set(a))
dic = {}
# 将去重后的列表值赋给字典的key
for i in b:
    dic[i] = 0
# 遍历原列表，字典中有则加1
for j in a:
    if j in dic.keys():
        dic[j] += 1
# 排序输出
print(sorted(dic.values(), reverse=True))

