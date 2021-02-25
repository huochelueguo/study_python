# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:04_排序相关(字典，列表).py
@Time:NAME.py@Time:2021/2/24 17:24
"""

"""
列表
"""

# 根据某个共有字段进行排序
list1 = [{"age": 20, "name": "a"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"}]
l2 = sorted(list1, key=lambda x: x['age'])
print(l2)
print('*' * 100)



"""
字典
"""

# 对字典的key值进行排序
dict1 = {2: 826, 3: 1120, 1: 2229, 4: 555}
print(sorted(dict1.keys()))
print('*' * 100)

# 对字典的value值进行排序
print(sorted(dict1.values()))
print('*' * 100)

# 对整个字典根据key值进行排序
l2 = dict1.items()
l3 = sorted(l2, key=lambda x: x[0])
dict2 = {}
for k,v in l3:
    dict2[k] = v
print(f'对整个字典根据key值进行排序{dict2}')
# 使用列表生成式改写
dict3 = {k:v for k,v in sorted(dict1.items(), key=lambda x: x[0])}
print(f'对整个字典根据key值进行排序{dict3}')
# 默认key为第一个值，因此可以省略为：
print({k:v for k,v in sorted(dict1.items())})
print('*' * 100)

# 对整个字典根据value值进行排序
ll2 = dict1.items()
ll3 = sorted(ll2, key=lambda x: x[1])
dict22 = {}
for k,v in ll3:
    dict22[k] = v
print(f'对整个字典根据value值进行排序{dict22}')
# 使用列表生成式改写
print({k:v for k,v in sorted(dict1.items(), key= lambda x: x[1])})