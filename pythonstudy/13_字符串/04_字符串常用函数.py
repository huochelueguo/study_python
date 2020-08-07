# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:04_字符串常用函数.py
@Time:NAME.py@Time:2020/8/7 16:52
"""
# find函数：查看sub是否在字符串中，在的话返回索引，且只返回第一次匹配到的索引；找不到返回-1
# 可以指定统计的范围，[start,end) 左闭区间右开区间
str = 'study python go go'
a = str.find('go')
print(a)    # 13
b = str.find('back')
print(b)    # -1

# count函数：统计子字符串的数量；可以指定统计的范围，[start,end) 左闭区间右开区间
c = str.count('o')
print(c)    # 3

# split函数：将字符串分割，默认根据空格进行分割
d = str.split()
print(d)    # ['study', 'python', 'go', 'go']
e = str.split('o', 1)
print(e)    # ['study pyth', 'n go go']

# replace:把字符串中的 old（旧字符串） 替换成 new(新字符串)，count代表最多替换多少次，默认-1代表全部替换
f = str.replace(' ', '-')   # study-python-go-go
print(f)
g = str.replace('go', 'gogo', 1)    # study python gogo go
print(g)

# join:字符串的拼接：将序列中的元素以指定的字符连接生成一个新的字符串
# 注意：必须满足条件为序列中的元素为字符，不能是数字，否则报错
li1 = ['1', '2', '3', '4']
h = '_'
i = h.join(li1)
print(i)    # 1_2_3_4

# upper/lower :大小写调整
j = str.upper()
print(j)    # STUDY PYTHON GO GO
k = j.lower()
print(k)    # study python go go

# isdigit:检查字符串是否只有数字
print(str.isdigit())    # False

# isalpha:检查字符串是否只有字母
print(str.isdigit())    # False,因为有空格

