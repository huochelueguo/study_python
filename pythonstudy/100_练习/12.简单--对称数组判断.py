# 要求：判断数组元素是否对称。例如[1，2，0，2，1]，[1，2，3，3，2，1]这样的都是对称数组
# 用Python代码判断，是对称数组打印True，不是打印False,如：


def duicheng(x):
    flag = True
    for i in range(int(len(x) / 2)):
        if x[i] != x[-i - 1]:
            # print('false')
            flag = False
            break
    print(flag)


a, b, c = [1, 2, 0, 2, 1], [1, 2, 3, 3, 2, 1], [1, 2, 3, 4, 5]
duicheng(a)
duicheng(b)
duicheng(c)
