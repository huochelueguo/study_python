#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 0004 23:16
# @Author  : sunze
# @File    : 05_自己实现简单迭代器.py


class iter_myself:

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            self.index += 1
            return self.data[self.index-1]
        else:
            raise StopIteration


# 使用迭代器遍历列表
my_list = [2, 3, 4, 56, 7]
my_iter = iter_myself(my_list)
for a in my_iter:
    print(a)