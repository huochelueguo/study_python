# 1.类似增加键值对的方法进行修改
# 2.只能修改value值，不呢修改key值
# 3.如果这个key值没有的话，就进行增加操作

dict1 = {
    "name": "zhangsan",
    "age": 20,
    "sex": "man",
    "weight": 75
}
print("输出未修改性别的字典")
dict1["sex"] = "women"
print("修改后的值")
print(dict1)
# 如果修改的值没有，就进行添加操作
dict1["height"] = 180
print(dict1)

