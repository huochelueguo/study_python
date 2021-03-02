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


def lenthoflist(testlist):
    n = len(testlist)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if testlist[i] > testlist[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp


if __name__ == '__main__':
    testlist = [3, 4, 1, 4, 7, 19, 10]
    final_list = lenthoflist(testlist)
    print(f'每个元素为终点的最长子序列值为:{final_list}')
    print(f'最长递增子序列值为:{max(final_list)}')

# 每个元素为终点的最长子序列值为:[1, 2, 1, 2, 3, 4, 4]
# 最长递增子序列值为:4