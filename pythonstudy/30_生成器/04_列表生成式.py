# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:04_列表生成式.py
@Time:NAME.py@Time:2020/8/8 15:15
"""

"""
生成[1x1, 2x2, 3x3, ..., 10x10]
"""
# 方法1，常规遍历方法
list1 = []
for i in range(1, 11):
    list1.append(i * i)
print(list1)

# 方法2：使用列表生成式,写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
li1 = [x * x for x in range(1, 11)]
print(li1)

"""
输出偶数的平方
"""
# 方法一：使用map
li2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(5):  # 该方法不推荐，因为每次删除一个元素后，列表长度都会减一，因此不确定循环次数很容易报错，可以将符合的元素插入到新的列表中
    if li2[i] % 2 != 0:
        li2.pop(i)
        print(li2)


def cheng(a):
    return a ** 2


data = map(cheng, li2)
print(list(data))
print('*' * 20)

# 方法二：使用map。优化版本，遍历列表，把符合条件的插入一个新的列表中
li3 = []
for i in li2:
    if i % 2 == 0:
        li3.append(i)

data = map(cheng, li3)
print(list(data))
print('*' * 20)

# 方法三：使用列表生成式
li4 = [x * x for x in range(1, 11) if x % 2 == 0]
print(li4)
print('*' * 20)


"""
列表生成式的多层嵌套
"""
li5 = [m + n for m in 'ABC' for n in 'abc']
print(li5)  # ['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']


# 练习：对该列表大小写进行调整L，除掉纯数字 = ['Hello', 'World', 18, 'Apple', None]
L = ['Hello', 'World', 18, 'Apple', None]
L2 = [a.lower() for a in L if type(a) == str]
print(L2)   # ['hello', 'world', 'apple']
