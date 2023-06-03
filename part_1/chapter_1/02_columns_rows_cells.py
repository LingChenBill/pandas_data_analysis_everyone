#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
查看数据的子集。

@Time: 2023/6/3
@Author: Lingchen
@Prescription: P45.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', sep='\t')
print(df.head())

# 获取特定列的数据。
country_df = df['country']
print(country_df.head())

# 显示末尾5行的数据。
print(country_df.tail())

# 获取多列数据。
subset = df[['country', 'continent', 'year']]
print(subset)

# error.
# df[0]

country_df = df['country']
print(type(country_df))

print(country_df)

# 若想要一个子集，请使用双括号，返回一个df类型的对象。
country_df_list = df[['country']]
print(type(country_df_list))

print(country_df_list)

