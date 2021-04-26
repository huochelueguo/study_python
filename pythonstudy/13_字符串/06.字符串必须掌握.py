# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:06.字符串必须掌握.py
@Time:2021/4/26 上午9:16
"""
"""
1.按照索引取值
2.切片（顾头不顾尾， 步长）
3.长度
4.成员运算in not in 
5.移除空白strip, lstrip, rstrip
6.切分split, rsplit
7.循环
8.无
9.lower,upper
10.startwith,endwith
11.format
12.join
13.replace
14.isdigjt
"""

# 切片
str = 'hello world'
print(str[0:5:-1])  # 输出为空，顺序为左至右，但是步长为负数，右向左
print(str[-1:-9:1]) # 同上
print(str[::-1])    # 反向输出
print(str[0:11:])   # 顾头不顾尾，因此要输出全部，一种为不带末尾下标，或者比末尾下标+1
print(str[-1:-12:-1])   # 逆向输出全部，需要下标+1
print(str[-1:]) # 起点为末尾，步长正1，因此仅保留d
print(str[-1::-1])  # 步长为负数，因此为全部字符
print('*' * 50)

# 成员运算
str1 = 'hello'
str2 = 'python'
print(str1 in str1)
print(str2 not in str)
print('*' * 50)

# 移除空白
str3 = '      hello world     '
print(f'未移除空白:{str3}.')
print(f'移除空白后:{str3.strip()}.')
print(f'移除左侧空白:{str3.lstrip()}.')
print(f'移除右侧空白:{str3.rstrip()}.')
print('*' * 50)

# 切分:默认按照空格切分，有2个参数，切分参考值和切的次数，返回值为切好的list
str4 = 'ni hao wo shi ni ge '
print(str4.split())
print(str4.split('i', 2))
print(str4.split('i'))

# 右侧切分：rsplit，功能同split,只是从右向左取值
print(str4.rsplit('i', 2))
print('*' * 50)

# join:多个字符串组合长一个新的字符串
print(str+'/'+str1+'/'+str2+'/'+str3+'/'+str4)
str5 = '111'
num = 444
print(str4+str5)
# print(str5+num) # 无法和数字相加
print('*' * 50)

# format
s='猪'
s1 = '牛'
s2 = '羊'
li = ['猪', '牛', '羊']
print('小明喜欢吃{}，不喜欢吃{}和{}.'.format(s,s1,s2)) # 使用format不需要带f,等同于下面
print(f'小明喜欢吃{s}，不喜欢吃{s1}和{s2}.')
print('小明喜欢吃{}，不喜欢吃{}和{}.'.format(li[0], li[1], li[2]))