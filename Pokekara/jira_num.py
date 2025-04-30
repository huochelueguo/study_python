#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2025/4/30 15:43
# @Author : sunwenxiao
# @File : jira_num.py
# @Software: PyCharm
import pandas as pd

# 读取Excel文件
df = pd.read_excel('/Users/sunwenxiao/Desktop/质量报告/2025/3-4/A_JIRA.csv')  # 替换为你的文件路径

# 统计每个经办人-解决结果的组合数量
result = df.groupby(['经办人', '解决结果']).size().unstack(fill_value=0)

# 创建透视表
pivot = pd.pivot_table(df,
                       index='经办人',
                       columns='解决结果',
                       values='主题',
                       aggfunc='count',
                       fill_value=0)

print(pivot)
pivot.to_excel('/Users/sunwenxiao/Desktop/透视表结果1.xlsx')
