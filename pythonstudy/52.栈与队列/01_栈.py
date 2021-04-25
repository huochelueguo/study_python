# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_栈.py
@Time:2021/3/12 上午9:00
"""

"""
概念:
    容器的一种，可以存入元素，访问元素，删除元素
特点：
    只能允许在容器的一侧（栈的顶端）进行插入（push）和读取数据（pop），保证任何时候访问、删除的元素都是最后存入的元素
**后进先出**
"""

"""
栈的列表实现
"""


class Stack(object):

    def __init__(self):     # 栈初始化
        self.stack = []

    def is_empty(self):     # 判断是否为空栈
        return self.stack == []

    def pop(self):      # 删除栈顶元素
        if self.is_empty():
            return 'empty stack'
        else:
            return self.stack.pop()

    def push(self, nums):   # 插入元素
        self.stack.append(nums)

    def top(self):  # 返回栈顶元素
        return self.stack[-1]

    def len(self):  # 返回栈长度
        return len(self.stack)


stack1 = Stack()
stack1.push(5)
stack1.push(4)
stack1.push(3)
stack1.push(2)
stack1.push(1)
print(stack1)
print(stack1.is_empty())
print(stack1.top())
print(stack1.len())
print(stack1.pop())
print(stack1.len())
print(stack1.top())