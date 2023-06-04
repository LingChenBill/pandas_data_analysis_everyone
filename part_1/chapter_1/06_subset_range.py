#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
利用range函数来获取df的column子集。

@Time: 2023/6/4
@Author: Lingchen
@Prescription: P58.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', sep='\t')
print(df.head())

small_range = list(range(5))
print(small_range)

subset = df.iloc[:, small_range]
print(subset)

# 获取 4-5 的整数列表。
small_range = list(range(3, 6))
print(small_range)

subset = df.iloc[:, small_range]
print(subset)

# IndexError: positional indexers are out-of-bounds
# 若整数越界了，就会出错。
# small_range = list(range(0, 8, 2))

# 获取 0, 2, 4 的整数列表。
small_range = list(range(0, 6, 2))
print(small_range)

subset = df.iloc[:, small_range]
print(subset)

