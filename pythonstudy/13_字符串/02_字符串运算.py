# 1.字符串拼接，直接使用+号即可连接
str1 = "hello"
str2 = str1 + " " + "python"
print("新字符串为：%s" % str2)

# 2.字符串重复输出，使用*
str1 = "hello"
print(str1 * 10)

# 3.取字符串某索引的值。类似列表，使用[]
str1 = "hello"
print(str1[0])

# 4.去字符串长度，使用len（）
str1 = "hello"
print(len(str1))

# 5.判断字符串中是否含有指定字段，in 或者 not in
str1 = "hello"
print("h" in str1)
print("1" not in str1)