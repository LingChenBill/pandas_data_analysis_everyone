#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
选择多列。loc与iloc使用。

@Time: 2023/6/3
@Author: Lingchen
@Prescription: P56.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', sep='\t')
print(df.head())

# 使用df.loc[:, [columns]]来获取列，: 指获取在这个维度的所有值。
subset = df.loc[:, ['year', 'pop']]
print(subset)

# iloc可以使用 整数 index.
subset_index = df.iloc[:, [2, 4, -1]]
print(subset_index)

# KeyError: "None of [Int64Index([2, 4, -1], dtype='int64')] are in the [columns]"
# subset = df.loc[:, [2, 4, -1]]
# print(subset)

# IndexError: .iloc requires numeric indexers, got ['year' 'pop']
# subset = df.iloc[:, ['year', 'pop']]
# print(subset)
