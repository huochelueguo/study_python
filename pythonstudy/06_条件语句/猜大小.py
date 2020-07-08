#输入数字和随机数比大小，直到两者大小一致，break判断
import  random
#随机生成一个整数
b = int(random.uniform(1,10))
print(b)
#输入一个数字，转换为整形
a = int(input ("请输入一个数字:"))
print(a)
while a != b:
    if a > b :
        print("大了，请重新输入")
        a = int(input("请输入一个数字:"))
    if a < b :
        print("小了，请重新输入")
        a = int(input("请输入一个数字:"))
    if a == b:
        print("OK，正好")
        break