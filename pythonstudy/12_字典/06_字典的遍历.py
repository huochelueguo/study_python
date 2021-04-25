"""
对于字典的遍历可以使用dict.items()
1。在python2X中，直接输出为一个list
2。在python3X中，输出为一个可迭代对象，防止数据过大影响效率，因此需要强转成list或者使用for进行迭代,结构为列表包元组[(),()]

对于key和value，可以使用dict.key dict.value进行单独遍历,返回值为一个list
"""

dict1 = {
    "name": 222,
    "age": 20,
    "sex": 0,
    "weight": 75
}

for key, value in dict1.items():
    print(key, value)

res = dict1.items() # 直接输出为dict1_items([key,value]组成的一个个元组)
#   dict_items([('name', 'zhangsan'), ('age', 20), ('sex', 'man'), ('weight', 75)])
print(list(res))    # 强转后生成一个list
print(type(res))
print('_' * 30)

print(f'对key进行单独遍历的结果{dict1.keys()}')
print(f'对value进行单独遍历的结果{dict1.values()}')

for k,v in enumerate(list(res)):
    print(k,v)