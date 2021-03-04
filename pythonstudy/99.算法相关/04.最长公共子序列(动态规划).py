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
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
"""


def longestCommonSubsequence(list1, list2):
    len_list1 = len(list1)
    len_list2 = len(list2)
    dp = [[0 for x in range(len_list1+1)] for y in range(len_list2+1)]
    for i in range(1, len_list1+1):
        for j in range(1, len_list2+1):
            if list1[i] == list2[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[len_list1][len_list2]







if __name__ == '__main__':
    A = [2,5,1,2,5]
    B = [10,5,2,1,5,2]
    print(longestCommonSubsequence(A, B))