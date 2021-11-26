# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 有效括号组合需满足：左括号必须以正确的顺序闭合。
class Solution:
    def generateParenthesis(self, n):
        res = []
        cur_str = ''
        def dfs(cur_str, left, right):
            if left == n and right == n:
                res.append(cur_str)
            if right > left:
                return res
            if left < n:
                dfs(cur_str+'(', left+1, right)
            if right < n:
                dfs(cur_str+')', left, right+1)
        dfs(cur_str, 0, 0)
        return res

n = 2
print(Solution().generateParenthesis(n))

