# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_copy.py
@Time:NAME.py@Time:2020/8/5 上午9:40
"""
import copy
# 对于不可变数据来说，不存在深浅拷贝，因此后续都说的是针对可变数据（包含子对象）
# 浅拷贝：数据版共享（复制数据在独立内存中存放，但是只成功拷贝了第一层,外部完全没关系，内部有关系）
li1 = [1, 2, 3, [4, 5, 6]]
li2 = copy.copy(li1)
print(li1, id(li1))
print(li2, id(li2))
# [1, 2, 3, [4, 5, 6]] 4380959552
# [1, 2, 3, [4, 5, 6]] 4381079360
print('* *' * 20)
li1[0] = 11
print(li1, id(li1))
print(li2, id(li2))
# [11, 2, 3, [4, 5, 6]] 4380959552
# [1, 2, 3, [4, 5, 6]] 4381079360
print('* *' * 20)
li2[3][0] = 666
print(li1, id(li1))
print(li2, id(li2))
print('* *' * 20)
# [11, 2, 3, [666, 5, 6]] 4536505536
# [1, 2, 3, [666, 5, 6]] 4536699008

# 浅拷贝对简单数据（不可变数据）来说，还是地址的引用，未开辟新的内存地址
a = 'abc'
b = copy.copy(a)
print(a, id(a))
print(b, id(b))
# abc 4503755376
# abc 4503755376
print('* *' * 20)
a = 'abcd'
print(a, id(a))
print(b, id(b))
# abcd 4504326704
# abc 4503755376
print('* *' * 20)
