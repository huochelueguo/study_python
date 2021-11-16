# # 给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。
# 示例 1：
#
# 输入：nums = [1,3,5,4,7]
# 输出：3
# 解释：最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。
# 示例 2：
#
# 输入：nums = [2,2,2,2,2]
# 输出：1
# 解释：最长连续递增序列是 [2], 长度为1。
# https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/

# 普通方法:
class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        n = len(nums)
        j = 1
        l = []
        if len(set(nums)) == 1:
            return 1
        else:
            for i in range(n-1):
                if nums[i+1] > nums[i]:
                    j +=1
                else:
                    j = 1
                l.append(j)
        return max(l)

# 动态规划
class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        n = len(nums)
        dp = [1] * n
        if len(set(nums)) == 1:
            return 1
        else:
            for i in range(1, n):
                if nums[i] > nums[i-1]:
                    dp[i] = dp[i-1] + 1


        return max(dp)