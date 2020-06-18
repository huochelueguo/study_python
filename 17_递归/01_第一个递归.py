# 如果一个函数在内部调用自身本身，这个函数就是递归函数。
# 简单的递归，求1-100的和
# 递归一定要有明确的边界，否则死循环


def sum(a):
    if a == 1:
        return a

    # print(a)
    summ = a + sum(a-1)
    # print(summ, a)
    return summ


b = sum(2)
print(b)
