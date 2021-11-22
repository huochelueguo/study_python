# 需求：每次洗牌，返回不一样的内容

# 方法1：使用自带模块
import random

list1 = [1, 3, 4, 5]
random.shuffle(list1)
print(list1)
print('-' * 50)


# 方法2：自己实现，遍历数组，用每一个数i和[i,len-1]区间内随机找一个数，进行互换，这样保证每个数都会被换一次，最后输出即可
def shuffle(s):
    l = len(list1)
    for i in range(l):
        j = random.randint(i, l - 1)
        list1[i], list1[j] = list1[j], list1[i]
    return s


print(shuffle(list1))
