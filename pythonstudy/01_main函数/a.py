#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 0002 23:27
# @Author  : sunze
# @File    : a.py


a = 100
print(a)
print(f'其他文件饮用时，a.py中name的值是{__name__}')

if "__name__" == "__main__":
    print(a)
    print(f'name的值是{__name__}')
# 在同文件下
#   __name__值为__main__
#  而在其他引用位置时
#   __name__的值为a
# 所以
#       对于一些只想在本文件内进行输出的内容，可以写在if "__name__" =="__main__"下面；此时其他的文件饮用时，不会被执行

