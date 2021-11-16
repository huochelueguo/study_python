# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。在「杨辉三角」中，每个数是它左上方和右上方的数的和
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 思路：每一行除去头尾的数字，都是上一行的同一列数字+同一列-1的数字之和
"""
1
11
121
1331
14641
"""

class Solution:
    def generate(self, numRows):
        n = numRows
        dp = [[1] * x for x in range(1, n + 1)]
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            for i in range(2, n):
                for j in range(i + 1):
                    if j == 0 or j == i:
                        continue
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            return dp


numRows = 5
s = Solution().generate(numRows)
print(s)
