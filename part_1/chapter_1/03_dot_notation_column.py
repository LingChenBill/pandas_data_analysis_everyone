#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
使用.来查看行数据，获取行和列数据。

@Time: 2023/6/3
@Author: Lingchen
@Prescription: P49.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', sep='\t')

country_df = df['country']
print(type(country_df))
print(country_df)

# 可以直接使用列的名称和.一起使用，但列名称中有空格，就不适用。
print(df.country)

print(df)

# 通过index来获取第一行。index 从0开始。
print(df.loc[0])
print(df.loc[99])

# 获取最后一行。
# KeyError: -1
# print(df.loc[-1])

# print(df.shape)
number_of_rows = df.shape[0]
last_row_index = number_of_rows - 1
print(df.loc[last_row_index])

print(df.tail(n=1))

subset_loc = df.loc[0]
subset_head = df.head(n=1)

# series.
print(type(subset_loc))
print(subset_loc)

# dataframe.
print(type(subset_head))
print(subset_head)

# 获取不同的行的集合。
print(df.loc[[0, 99, 999]])
