#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 连接不同的索引。

@Time: 2023/6/19
@Author: Lingchen
@Prescription: P283.
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

# 重命名列名。
df1.columns = ['A', 'B', 'C', 'D']
df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']
print(df1)
print(df2)
print(df3)

# 列自身对齐，NaN 填充所有缺失的区域。
row_concat = pd.concat([df1, df2, df3])
print(row_concat)

# 如果我们试图只保留所有三个数据帧中的列，我们将得到一个空的数据帧，因为没有共同的列。
print(pd.concat([df1, df2, df3], join='inner'))

# 如果我们使用具有共同列的数据帧，则只返回所有列共享的列。
print(pd.concat([df1, df3], ignore_index=False, join='inner'))
