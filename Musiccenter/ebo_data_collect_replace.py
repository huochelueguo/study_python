#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2025/5/9 16:42
# @Author : sunwenxiao
# @File : ebo_data_collect.py
# @Software: PyCharm


# 服务端ebo导入没有按照liuyujia给的顺序导入，所以要把导入song_id，到yujia的Excel中找到，生成一个新的Excel，代码主要对替换歌曲进行操作

import pandas as pd

# 读取 Excel1：导入的1000个song_id
df1 = pd.read_excel("/Users/sunwenxiao/Desktop/EBO/ebo上线歌曲列表.xlsx")


# 读取 Excel2（大数据集）
df2 = pd.read_excel("/Users/sunwenxiao/Desktop/EBO/yujia表格_替换.xlsx")


# 方法1：使用merge进行左连接（推荐）
result = pd.merge(df1, df2, on='song_id', how='left')


# 检查未匹配到的song_id
missing_ids = df1[~df1['song_id'].isin(df2['song_id'])]['song_id']
if not missing_ids.empty:
    print(f"以下song_id在表格2中未找到: {missing_ids.tolist()}")

# 保存结果到新Excel文件
result.to_excel('/Users/sunwenxiao/Desktop/EBO/匹配结果_替换歌曲.xlsx', index=False)

print("匹配完成，结果已保存到'匹配结果.xlsx'")