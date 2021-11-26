# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:07.最长回文子串(动态规划)-no.py
@Time:NAME.py@Time:2021/3/8 16:06
"""

class Solution:
    def longestPalindrome(self, s):
        len1 = len(s)
        dp = [[False]*len1 for j in range(len1)]
        max_lenth = 1
        start = 0
        cur_len = 0
        for k in range(len1):
            dp[k][k] = True
        for j in range(1, len1):
            for i in range(0, j):
                if j - i <=2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        cur_len = j-i+1
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                        cur_len = j-i+1
                if dp[i][j] == True:
                    # 当为true时，意味着为回文，记录回文的起点为i，长度方面，因为不包尾，因此是j-i+1
                    # 比如babad，j为3、i为1时为最大回文，因此区间为[1~3]，
                    # 所以在切片时要在默认加上起始值也就是[1:4],输出aba
                    if cur_len>max_lenth:
                        max_lenth = cur_len
                        start = i
        print(dp)
        return s[start:start+max_lenth]

s = 'acbbcca'
print(Solution().longestPalindrome(s))