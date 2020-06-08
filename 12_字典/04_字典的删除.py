# 1.删除字典得方法，通过del关键字
dict1 = {
    "name": "zhangsan",
    "age": 20,
    "sex": "man",
    "weight": 75
}
del dict1["age"]
print("删除年龄后的新字典 %s" % dict1)

# 2.将字典内容清空，也是通过del关键字，但是字典名称后面不带KEY值
# 但这会引发一个异常，因为用del后字典不再存在
dict1 = {
    "name": "zhangsan",
    "age": 20,
    "sex": "man",
    "weight": 75
}
del dict1
# 输出后报错：NameError: name 'dict1' is not defined
#print("字典使用del关键字清空 %s" % dict1)

# 3.使用clear关键字，清空字典，再次输出为空字典｛｝
dict1 = {
    "name": "zhangsan",
    "age": 20,
    "sex": "man",
    "weight": 75
}
dict1.clear()
print("使用clear关键字清空得字典 %s" % dict1)

