# 1.字典遍历专门的函数，字典名.items()，可以使用for循环直接遍历输出
dict1 = {
    "name": "zhangsan",
    "age": 20,
    "sex": "man",
    "weight": 75
}

for key, value in dict1.items():
    print(key, value)


