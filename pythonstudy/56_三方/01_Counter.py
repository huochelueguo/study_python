"""
Counter：属于字典的子类，因此适用于dict相关的方法
    主要作用：
    1、统计数据出现的次数，以字典的形式返回，且按照出现次数降序返回
    2、根据创建的counter，可以生成对应的数据

"""
from collections import Counter

li = [1, 2, 3, 4, 5, 6, 1, 2, 5, 5, 5]
s = Counter(li)
print(type(s))
print(f'各数字出现的次数是：{s}')  # Counter({5: 4, 1: 2, 2: 2, 3: 1, 4: 1, 6: 1})

# 也可以对counter后的值进行排序
print(sorted(s.items(), key=lambda x: x[1]))

# 对某个书进行赋值
s[6] = 10
print(s)  # Counter({6: 10, 5: 4, 1: 2, 2: 2, 3: 1, 4: 1})

# 将s置为空
s.clear()
print(s)  # Counter()
print('*' * 50 + '生成相关数据' + '*' * 50)
c = Counter()    # 创建一个新的空counter
c2 = Counter(a=4, b=2, c=0, d=-2)   # 非空的counter
l2 = list(c2.elements())    # 通过element可以将counter中的数据转换城列表
print(l2)   # ['a', 'a', 'a', 'a', 'b', 'b']
