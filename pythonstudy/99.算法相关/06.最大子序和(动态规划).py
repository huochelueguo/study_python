# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:06.最大子序和(动态规划).py
@Time:2021/3/10 上午9:23
"""
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
"""

def maxsum(testlist):
    m = len(testlist)
    for i in range(1, m):
        testlist[i] = max(testlist[i], testlist[i] + testlist[i-1])
    return max(nums)


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxsum(nums))