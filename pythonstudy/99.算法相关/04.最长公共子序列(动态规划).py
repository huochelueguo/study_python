# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:04.最长公共子序列(动态规划).py
@Time:2021/3/4 上午8:59
"""
"""
题目：
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度【非连续】。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
"""


def longestCommonSubsequence(txt1, txt2):
    m = len(txt1)
    n = len(txt2)
    # 设置辅助二维数组，初始值每个都是0，如横向为m，竖向为n
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    print(dp)
    # 注意：是循环对比：横向不变，和竖向每一个值对比，相等则是各-1值加1，否则为辅助数组中两个的最大值
    """
    如果 m != n，二维数组mn的顺序要和循环时相反
    """
    for i in range(1, m+1):
        for j in range(1, n+1):
            if txt1[i-1] == txt2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return max(max(dp))


if __name__ == '__main__':
    lis = 'abcde'
    lis2 = 'ace'
    print(longestCommonSubsequence(lis, lis2))