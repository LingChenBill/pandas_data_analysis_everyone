#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 不同的列进行连接。

@Time: 2023/6/20
@Author: Lingchen
@Prescription: P245.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df1 = pd.read_csv('../../data/concat_1.csv')
df2 = pd.read_csv('../../data/concat_2.csv')
df3 = pd.read_csv('../../data/concat_3.csv')

print(df1)
print(df2)
print(df3)

# 重新命名列名。
df1.columns = ['A', 'B', 'C', 'D']
df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']

# 修改索引。
df1.index = [0, 1, 2, 3]
df2.index = [4, 5, 6, 7]
df3.index = [0, 2, 5, 7]

print(df1)
print(df2)
print(df3)

# 当沿着 axis="columns" (axis=1) 连接时，新的数据帧将以逐列的方式添加，并与它们各自的行索引相匹配。
# 缺失值指示符出现在索引未对齐的区域。
col_concat = pd.concat([df1, df2, df3], axis='columns')
print(col_concat)

col_concat_axis = pd.concat([df1, df2, df3], axis=1)
print(col_concat_axis)

# 正如我们以行方式连接时所做的那样，我们可以通过使用 join="inner" 选择仅在存在匹配索引时保留结果。
print(pd.concat([df1, df3], axis='columns', join='inner'))
