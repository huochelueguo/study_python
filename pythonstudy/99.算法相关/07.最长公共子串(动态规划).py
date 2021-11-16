# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:07.最长公共子串(动态规划).py
@Time:2021/11/15 9:38 上午
"""
# 最长公共子串：两个字符串中连续相等的最长子串。
# 和最长公共子序列区别：这个要求是连续的，最长公共子序列为非连续
# 思路：和子序列类似，但是当两个数组值不想等时，dp[i][j]就不需要取大值，应该设置为0，其他都是一样的
# https://www.cnblogs.com/yuling-chao/p/7383096.html


def findLongest(list1, list2):
    m = len(list1)
    n = len(list2)
    dp = [[0 for x in range(n+1)] for y in range(m+1)]
    longest = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            # if i == 0 or j == 0:
            #     dp[i][j] = 0
            # elif list1[i-1] == list2[j-1]:
            if list1[i-1] == list2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if longest < dp[i][j]:   # 记录每次的值，和最大值相比，替换最大值，最后返回
                    longest = dp[i][j]
            else:
                dp[i][j] = 0

    print(longest)
    print((dp))
    return longest


if __name__ == '__main__':
    lis = 'abcde'
    lis2 = 'abce'
    print(findLongest(lis, lis2))