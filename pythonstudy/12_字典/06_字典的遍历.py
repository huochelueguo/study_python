# 1.字典遍历专门的函数，字典名.items()，可以使用for循环直接遍历输出
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

res2 = sorted(list(res), key = lambda x : x[0])
print(dict(res2))