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


