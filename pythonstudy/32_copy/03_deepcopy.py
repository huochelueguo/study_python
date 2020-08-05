# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03_deepcopy.py
@Time:NAME.py@Time:2020/8/5 下午11:48
"""
# 深拷贝
# 当拷贝对象没有子对象时，深浅拷贝意义一致
import copy
a = [1, 2, 3, 4]
b = copy.deepcopy(a)
print(a, id(a))
print(b, id(b))
print('* *' * 20)
# [1, 2, 3, 4] 4567846528
# [1, 2, 3, 4] 4567844160
b[0] = 111
print(a, id(a))
print(b, id(b))
print('* *' * 20)
# [1, 2, 3, 4] 4450307456
# [111, 2, 3, 4] 4450305088

# 当有子对象时，深拷贝对于拷贝对象，相当于创建了个完全新的对象，和原对象无一点关系
c = [1, 2, 3, 4, [5, 6, 7]]
d = copy.deepcopy(c)
print(c, id(c))
print(d, id(d))
print('* *' * 20)
# [1, 2, 3, 4, [5, 6, 7]] 4450485952
# [1, 2, 3, 4, [5, 6, 7]] 4450486016
d[0] = 'a'
d[4][0] = 555
print(c, id(c))
print(d, id(d))
print('* *' * 20)
# [1, 2, 3, 4, [5, 6, 7]] 4450485952
# ['a', 2, 3, 4, [555, 6, 7]] 4450486016
