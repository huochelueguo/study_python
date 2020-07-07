# 1.查询字典中某个值,查询对应键值即可，但是没有对应键值可能报错
dict1 = {
    "name": "zhangsan",
    "age": 20,
    "sex": "man",
    "weight": 75
}

str = dict1["age"]
print("age:", str)

# 2.防止报错，可以使用get来获取键值，即使找不到也不会报错
dict1 = {
    "name": "zhangsan",
    "age": 20,
    "sex": "man",
    "weight": 75
}
# 使用get时，括号中不需要方括号
str = dict1.get('key3')
print("key3:", str)



