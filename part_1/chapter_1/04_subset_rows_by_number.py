#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
按行号设置子行。

@Time: 2023/6/3
@Author: Lingchen
@Prescription: P54.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', sep='\t')
print(df.head())

# 第二行。
print(df.iloc[1])

# 最后一行。
print(df.tail())
print(df.iloc[-1])

# 多行。
print(df.iloc[[0, 99, 999]])
