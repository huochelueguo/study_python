# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:13_sorted函数.py
@Time:2020/10/23 上午9:25
"""
# 函数作用：对所有可以迭代对象进行排序，并生成一个新的对象，对原对象内容不作修改
# 对纯数字列表进行排序
list1 = [1, 999, 4, 51, 200, 88, 23]
print(sorted(list1))    # [1, 4, 23, 51, 88, 200, 999]

# 对嵌套字典数组进行排序
li2 = [{"age": 20, "name": "a"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"}]
# li2.sort()
# print(li2)  # 报错：TypeError: '<' not supported between instances of 'dict' and 'dict'
print(sorted(li2, key=lambda x: x["age"]))

# 对字典进行排序
dict1 = {2: 86, 3: 20, 1: 9, 4: 555}
# 对字典的key值进行排序
print(sorted(dict1.keys()))   # [1, 2, 3, 4]

# 对字典value值进行排序
print(sorted(dict1.values()))  # [9, 20, 86, 555]

# 对整个字典根据key值进行排序
li3 = dict1.items()
li4 = sorted(li3)
dict2 = {}
for k, v in li4:
    dict2[k] = v
print(dict2)

# 对整个字典根据value值进行排序
li5 = sorted(dict1.items(), key=lambda key: key[1], reverse=True)
dict3 = {}
for k, v in li5:
    dict3[k] = v

    # 以上代码可以简化成一句话
dict4 = {k: v for k, v in sorted(dict1.items(), key=lambda key: key[1], reverse=True)}
print(dict3)
print(dict4)


# practice
dict5 = {2: 96, 5: 100, 10: 82, 1: 55}
print(dict5)
l1 = dict5.items()
l2 = sorted(l1, key=lambda key: key[1], reverse=True)
dict6 = {k: v for k, v in l2}
print(dict6)
