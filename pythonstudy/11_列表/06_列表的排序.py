# 使用sort进行排序
# 注意1：使用sort/reverse排序时，先对list排序后，在进行print，不能够在输出中进入排序，这样输出为none
# 注意2：直接使用sort/reverse排序，相当于改变了原列表值
list1 = [1, 3, 5, 2, 9, 8, 40, 21]
print(list1.sort())     # 输出为none
list1.sort()
print(list1)    # 输出[1, 2, 3, 5, 8, 9, 21, 40]
list1.reverse()
print(list1)    # 输出[40, 21, 9, 8, 5, 3, 2, 1]
list1.sort(reverse=True)
print(list1)    # 输出[40, 21, 9, 8, 5, 3, 2, 1]

# 使用sorted函数排序
# 参考28_内置函数和模块中内容

