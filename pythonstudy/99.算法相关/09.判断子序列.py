# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

# 思路：遍历判断当i在t里面时，使用切片调整l2

class Solution:
    def isSubsequence(self, s, t) :
        l1 = list(s)
        l2 = list(t)
        len1 = len(l1)
        len2 = len(l2)
        l = []
        if len1>len2:
            return False
        else:
            for i in l1:
                if i in l2:
                    l2 = l2[(l2.index(i))+1::]
                else:
                    return False
            return True if sorted(l) == l else False