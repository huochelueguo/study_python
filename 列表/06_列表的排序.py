#1.通过sort进行正序排序，非数字型根据个元素首字母书序排序
list1 = [6, 2, 3, 4]
list1.sort()
print(list1)
#输出为['a', 'c', 'r', 'w']
lista = ['c', 'w', 'r', 'a']
lista.sort()
print(lista)


#2.通过sort(reverse=True)进行倒序排序
list1 = [1, 3, 4, 5]
list1.sort(reverse=True)
print(list1)

#3.通过reverse逆序排序，和大小无关
list1 = [4, 5, 1, 6, 'a', 'g']
list1.reverse()
print(list1)