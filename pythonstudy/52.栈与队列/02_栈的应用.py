# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_栈的应用.py
@Time:NAME.py@Time:2021/3/12 15:21
"""

"""
括号匹配问题
https://www.cnblogs.com/superhin/p/11454799.html
思路：利用字典和栈的思想，将括号作为一个字典，为左括号时插入到栈里面，是右括号时取出栈顶进行对比
"""


def is_closed(txt):

    kuohao_dict = {')': '(', ']': '[', '}': '{'}
    stack = []
    for i in txt:
        if i in kuohao_dict.values():   # 最先开始的是左侧括号，因此如果是左括号，插入栈中
            stack.append(i)
        elif i in kuohao_dict.keys():   # 如果是右括号，那就将i和栈中最外侧的一个值比较，如果相同，则删除最外侧，否则报false
            # if kuohao_dict[i] == stack[-1]:
            #     stack.pop()
            # else:
            #     return False
            if kuohao_dict[i] != stack.pop():   # 等同于上方注释代码
                return False

    return True


text = "({[({{abc}})][{1}]})2([]){({[]})}[]"
text2 = '{[]}'
text3 = '{}{}[]'
print(is_closed(text2))

