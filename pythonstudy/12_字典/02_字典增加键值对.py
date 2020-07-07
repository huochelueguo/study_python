# 直接使用字典[]=XX来进行新键值对赋值，但是KEY值不呢重复，否则报错

dict1 = {
    "name": "zhangsan",
    "age": 20,
    "sex": "man",
    "weight": 75
}
print(dict1)
dict1["height"] = 172
print(dict1)
