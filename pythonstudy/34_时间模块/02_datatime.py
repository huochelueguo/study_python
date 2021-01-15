# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_datatime.py
@Time:NAME.py@Time:2020/8/7 20:32
"""
# datatime模块
from datetime import datetime, timedelta  # 导入datatime模块中的datatime类

# 获取当前时间，返回直接可以使用的格式得数据
print(datetime.now())   # 2020-08-07 20:48:09.880275

# 获取时间差：timedelta
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
current_time = datetime.now()   # 2020-08-07 20:53:00.042729
new1 = current_time + timedelta(days=10)    # 2020-08-17 20:53:00.042729
print(new1)
new2 = current_time + timedelta(hours=24)   # 2020-08-08 20:53:35.386716
print(new2)

# 时间格式转换为字符串时间,和time模块一致，都是使用 时间.strftime('时间格式')
now_time = datetime.now()
print(now_time.strftime('%Y/%m/%d %H:%M'))

# 字符串格式时间转换为时间格式,转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串
str_time = '2020/08/08 20:57:43'
data_time = datetime.strptime(str_time, '%Y/%m/%d %H:%M:%S')
print(str_time, type(str_time))     # 2020/08/08 20:57:43 <class 'str'>
print(data_time, type(data_time))   # 2020-08-08 20:57:43 <class 'datetime.datetime'>


