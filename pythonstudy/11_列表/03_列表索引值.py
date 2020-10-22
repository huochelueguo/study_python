# 通过index求列表某一个元素第一次出现的位置
list1 = [2, 4, 4, 5, 6]
print(list1.index(4))

for suoyin in list1:
    if suoyin == 4:
        print(list1.index(suoyin))

a = 2
if a not in list1:
    list1.append(8)
    print(list1)
else:
    print(list1.index(a))