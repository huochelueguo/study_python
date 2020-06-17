# 通过append，加在末尾，只允许添加一个
# 添加多个报错append() takes exactly one argument (2 given)

list1 = [1, 2, 3, 4, 5, 6]
list1.append(7)
print(list1)

# 通过insert，指定插入位置
list2 = [1, 2, 3, 4, 5, 6]
list2.insert(0, 999)
print(list2)

# 通过extend，将两个列表合并
list3 = [1, 2, 3, 4, 5]
list4 = [1, 2, 3, 4, 5, 6]
list3.extend(list4)
print(list3)
