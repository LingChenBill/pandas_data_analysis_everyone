#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
使用切片来获取df子集。

@Time: 2023/6/4
@Author: Lingchen
@Prescription: P60.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', sep='\t')
print(df.head())

print(df.columns)

small_range = list(range(3))
subset = df.iloc[:, small_range]
print(subset)

# 切片前 3 列。
subset_slice = df.iloc[:, :3]
print(subset_slice)

small_range = list(range(3, 6))
subset = df.iloc[:, small_range]
print(subset)

subset_slice = df.iloc[:, 3:6]
print(subset_slice)

small_range = list(range(0, 6, 2))
subset = df.iloc[:, small_range]
print(subset)

subset_slice = df.iloc[:, 0:6:2]
print(subset_slice)

# 整个列表(0~5).
subset_slice = df.iloc[:, 0:6:]
print(subset_slice)

# 以2为切片步长，0 2 4.
subset_slice = df.iloc[:, 0::2]
print(subset_slice)

# 以2为切片步长，切到6之前。
subset_slice = df.iloc[:, :6:2]
print(subset_slice)

# 整个列表切片。
subset_slice = df.iloc[:, ::]
print(subset_slice)
