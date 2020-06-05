#列表删除方法
#1.通过pop，无参数时默认删除最后一个元素
list1 = [1, 2, 3, 4]
list1.pop()
print(list1)


#2.通过pop，加参数
list1 = [1, 2, 3, 4]
list1.pop(2)
print(list1)

#3.通过del,删除指定索引元素
list1 = [1, 2, 3, 4]
del list1[0]
print(list1)

#4.通过clear，清空列表
list1 = [1, 2, 3, 4]
list1.clear()
print(list1)

#5.通过remove，删除第一个出现的指定数据
list1 = [1, 1, 2, 3, 4]
list1.remove(1)
print(list1)
