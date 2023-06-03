#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
加载数据。
查看数据的类型和属性。

@Time: 2023/6/3
@Author: Lingchen
@Prescription: P43.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', sep='\t')

print(df)

print(type(df))

# 查看df的行和列。
print(df.shape)

# 获取列名。
print(df.columns)

# 列的属性。
print(df.dtypes)
print(df.info())
