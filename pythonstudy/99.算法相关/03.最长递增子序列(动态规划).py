# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:03.最长递增子序列(动态规划).py
@Time:NAME.py@Time:2021/3/2 11:38
"""

"""
使用动态规划实现最长递增子序列

"""


# 最长递增子序列最长值
def lenthoflist(testlist):
    n = len(testlist)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if testlist[i] > testlist[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp


# 最长递增子序列列表
def longlist(testlist, dp):
    n = max(dp)     # dp数组中最大值，即递增子序列的长度：3
    lis = [0] * n   # 创建递增子序列：【0，0，0】
    index = dp.index(n)  # dp数组中最大值的索引下标：4
    n -= 1  # 最大值为n，数组下标从0开始，因此-1
    lis[n] = testlist[index]    # 递增子序列列表最大值赋值：【0，0，49】
    for i in range(index-1, 0, -1):
        if testlist[i] < testlist[index] and dp[index] - 1 == dp[i]:
            # 求最长递增子序列时，如果i大于j且j的维护数组大于i的，会+1，这里属于逆向思维，-1
            n -= 1  # 数组下标从0开始，因此赋值时需要-1
            index = i   # 当满足条件后，循环起始值需要调整为新的，也就是从i开始再找就可以
            lis[n] = testlist[i]
            print(f'%%{lis}')
    return lis


if __name__ == '__main__':
    testlist = [3, 1, 24, 15, 49]
    #     dp = [1, 1, 2, 2, 3]
    final_list = lenthoflist(testlist)
    print(f'每个元素为终点的最长子序列值为:{final_list}')
    print(f'最长递增子序列值为:{max(final_list)}')
    dp = final_list
    print(longlist(testlist, dp))

# 每个元素为终点的最长子序列值为:[1, 2, 1, 2, 3, 4, 4]
# 最长递增子序列值为:4