#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2025/5/9 16:42
# @Author : sunwenxiao
# @File : ebo_data_collect.py
# @Software: PyCharm


# 服务端ebo导入没有按照liuyujia给的顺序导入，所以要把导入song_id，到yujia的Excel中找到，生成一个新的Excel，代码主要对替换歌曲进行操作

import pandas as pd

# 读取 Excel1：新增歌曲歌曲名称
df1 = pd.read_excel("/Users/sunwenxiao/Desktop/EBO/匹配结果_新增歌曲.xlsx")


# 读取 Excel2（大数据集）
df2 = pd.read_excel("/Users/sunwenxiao/Desktop/EBO/yujia表格_新增.xlsx")


# 基于曲名和歌手名进行完全匹配合并
merged_df = pd.merge(
    df1,
    df2,
    on=['曲名', '歌手名'],  # 同时匹配两个字段
    how='left'  # 保留表格1中所有记录，即使表格2中没有匹配项
)

# 检查未匹配的记录
# unmatched = merged_df[merged_df['作詞者'].isna()]
# if not unmatched.empty:
#     print("以下歌曲未找到匹配信息:")
#     print(unmatched[['曲名', '歌手名']].to_string(index=False))

# 保存结果到新Excel文件
merged_df.to_excel('/Users/sunwenxiao/Desktop/合并结果.xlsx', index=False)

print("合并完成，结果已保存到'合并结果.xlsx'")
