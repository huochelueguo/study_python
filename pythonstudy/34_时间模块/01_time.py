# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01_time.py
@Time:NAME.py@Time:2020/8/7 18:56
"""
# 只能表示1970-2038年的时间，常用的几个函数
import time

# time.time：返回当前时间戳. 时间戳：时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量
print(time.time())

# time.localtime([sec])：将一个时间戳转化成一个当时时区的struct_time，如果sec参数未输入，则以当前时间为转化标准
print(time.localtime())

# time.strftime(format[,t])：
# 把一个代表时间的元组或者struct_time转化为格式化的时间字符串。
# 将时间元组或 struct_time 对象格式化为指定格式的时间字符串。如果不指定参数 t，则默认转换当前时间；
print(time.strftime('%Y-%m-%d %H:%M:%S'))   # 2020-08-07 20:39:50

