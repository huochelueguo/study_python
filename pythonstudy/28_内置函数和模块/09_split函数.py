# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:09_split函数.py
@Time:NAME.py@Time:2020/7/22 上午9:06
"""
# 函数作用：分割字符串,将字符串分割为列表

str = 'my name is xiaoming'
print(f'默认按照空格分段输出{str.split()}')


str = '/Users/sunwenxiao/PycharmProjects/study_python/pythonstudy/28_内置函数和模块/09_split函数.py'
list_str = str.split("/", 8)
print(list_str)
# 输出['', 'Users', 'sunwenxiao', 'PycharmProjects', 'study_python', 'pythonstudy', '28_内置函数和模块', '09_split函数.py']


str = '/Users/sunwenxiao/PycharmProjects/study_python/pythonstudy/28_内置函数和模块/09_split函数.py'
list_str = str.split('/', 10)[2]
print(f'根据/分割网址后，第二个模块中内容是：{list_str}')  # 输出为sunwenxiao

# split的嵌套，如下获取www.baidu.com
str = "hello boy<[www.baidu.com]>byebye"
list1 = str.split('[')[1].split(']')[0]
print(list1)
