import pandas as pd
import numpy as np

file_path = '/Users/sunwenxiao/Desktop/test.xlsx'
# 默认读取前5行，df.head()，head后面也可以加参数
df = pd.read_excel(file_path)
print(df.head())
print('*' * 50)

# 默认读取后5行，df.tail(),括号中可以加参数
df = pd.read_excel(file_path)
# 输出后10行
print(df.tail(10))
print('*' * 50)

# 索引操作
#   不包含第一行
#   df.iloc[行索引,列索引]（索引从0开始，输出内容含首不含尾）
#   行索引：表示需要选取那几行
#   列索引：表示需要选取那几列

# 选择某几行
df = pd.read_excel(file_path)
print(df.iloc[3:8, :])
print('*' * 50)

# 选择某几列:
# 如果我们要跨列选取，得先把位置参数构造成列表形式，这里就是[0,4]，
# 如果是连续选取，则无需构造成列表，直接输入0:5
# 1.连续列，使用x:y
df = pd.read_excel(file_path)
print(df.iloc[:, 0: 1])
print('*' * 50)
# 2.跨列选择，使用[x,y]
df = pd.read_excel(file_path)
print(df.iloc[:, [0, 2]])
print('*' * 50)

# 行列交叉选择：将行列选择合并到一起，选择对应的索引
df = pd.read_excel(file_path)
# 输出部分姓名和年年
print(df.iloc[3:8, 0:2])
print('*' * 50)

# 基于名称（标签）的索引
# 筛选出第一列满足的值：df['姓名'] == '小米'，返回结果是true/false
# 使用df.loc根据筛选出来的值，展示true的内容
df = pd.read_excel(file_path)
print(df['姓名'] == '小米')
print(df.loc[df['姓名'] == '小米', :])
