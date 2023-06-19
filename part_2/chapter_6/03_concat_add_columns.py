#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 添加列。

@Time: 2023/6/19
@Author: Lingchen
@Prescription: P281.
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

# 连接列与连接行非常相似。主要区别在于 concat 函数中的 axis 参数。
# axis 的默认值为0 (或"index")，因此它将按行连接数据。
# 但是，如果我们将 axis=1 (或axis="columns") 传递给函数，它将按列连接数据。
col_concat = pd.concat([df1, df2, df3], axis='columns')
print(col_concat)

# 获取 'A' 列。
print(col_concat['A'])

# 直接添加一列。
col_concat['new_col_list'] = ['n1', 'n2', 'n3', 'n4']
print(col_concat)

# 通过 Series 来添加新的 列。
col_concat['new_col_series'] = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(col_concat)

# 可以重置列索引，这样就不会有重复的列名。
print(pd.concat([df1, df2, df3], axis='columns', ignore_index=True))
