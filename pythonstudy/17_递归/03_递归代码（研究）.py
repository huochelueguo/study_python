#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 0028 17:38
# @Author  : sunze
# @File    : 03_递归代码（研究）.py

def func4(x):
    print(1)
    if x>0:
        print(f'处理前{x}')
        func4(x-1)
        print(f'处理后{x}')

func4(4)

# 输出
# 处理前4
# 1
# 处理前3
# 1
# 处理前2
# 1
# 处理前1
# 1
# 处理后1
# 处理后2
# 处理后3
# 处理后4