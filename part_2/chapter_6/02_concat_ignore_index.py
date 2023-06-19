#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 连接数据，忽略 index。

@Time: 2023/6/19
@Author: Lingchen
@Prescription: P280.
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

# 如果我们只是想将数据连接或追加在一起，我们可以使用 ignore_index 参数在连接后重置行索引。
row_concat_i = pd.concat([df1, df2, df3], ignore_index=True)
print(row_concat_i)
