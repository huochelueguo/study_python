# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""
思路：n为1时，只有1种方法，
n为2时，有2种方法1+1； 2，
n为3时，有3种方法：1+1+1； 2+1； 1+2
n为4时，只可能从2或者3进入到1，因此f(4) = f(3) + f(2) = 5种:1+1+1+1； 2+1+1；1+2+1； 1+1+2； 2+2；
由此可知，当n大于2时，方法数等于(n-1)和（n-2）的和，类似于斐波那契数列
"""


def methods(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


# 使用递归实现斐波那契数列
def methods2():
    a = b = 1
    while True:
        yield a
        a, b = b, a+b


num = 4
print(methods(num))

g = methods2()
l = []
# 因为上楼梯是从1个台阶开始，因此循环时要多循环一次[1, 2, 3, 5...]
for i in range(num+1):
    l.append(next(g))
print(l[-1])


