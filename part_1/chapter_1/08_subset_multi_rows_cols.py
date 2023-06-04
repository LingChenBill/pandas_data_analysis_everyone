#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
获取复数的行和列数据。

@Time: 2023/6/4
@Author: Lingchen
@Prescription: P64.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', sep='\t')
print(df.head())

print(df.loc[3, 'country'])
print(df.iloc[3, 0])

# KeyError: 0
# print(df.loc[3, 0])

print(df.iloc[[0, 99, 999], [0, 3, 5]])

# 尽量使用label，index可能会变化。这时经使用 loc 不能是 iloc.
print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])

# loc 匹配名称值， iloc 匹配位置。
print(df.loc[10:13:])

print(df.iloc[10:13:])
