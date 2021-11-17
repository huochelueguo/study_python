# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:12. 股票买入时机01.py
@Time:2021/11/18 12:06 上午
"""


class Solution:
    def maxProfit(self, prices):
        dp = [0] * len(prices)
        buy_money = prices[0]  # 购买的初始价格为第一天的价格
        if len(prices) < 2:
            return 0
        else:
            for i in range(1, len(prices)):
                if prices[i] > buy_money:     # 如果第二天的购买价格大于初始价格，那么当天的收益就是卖出价-初始低价
                    dp[i] = prices[i] - buy_money
                else:
                    buy_money = prices[i]     # 如果第二天购买的价格小于初始价格，那么初始价格将会更新，
        print(dp)
        return max(dp)


s = [7,1,5,3,6,4]
# dp =[0,0,0,0,0,0]
# 初始购买价格为第一天的7，循环第一次卖出为1，因为1-7为负数，因此收益为负数，dp[1]为0和负数无所谓，因此不更新，但是买入价小于第一天因此更新price_first
# 第二次循环时，卖出为5，大于初始买入价格，因此dp[2] = 4,因此不在更新最小买入价，此时dp=[0,0,4,0,0,0]
# 第三次循环时，同第二次逻辑，此时dp=[0,0,4,2,0,0]
# 第四次循环时，同第二次逻辑，此时dp=[0,0,4,2,5,0]
# 最后一次循环，同第二次逻辑，此时dp=[0,0,4,2,5,3]
print(Solution().maxProfit(s))