#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 通过 Recode 和 Replace 来处理缺失值。

@Time: 2023/6/28
@Author: Lingchen
@Prescription: P368.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

ebola = pd.read_csv('../../data/country_timeseries.csv')
print(ebola.head())

# 使用 .fillna() 方法将丢失的值重新编码为另一个值。
# 将缺失的值填充为0，只查看前5列。
print(ebola.fillna(0).iloc[:, 0:5])

# 可以使用内置方法向前或向后填充。
# 向前填充数据时，上一个已知值（从上到下）将用于下一个丢失的值。
# 这样，丢失的值将替换为上一个知道和记录的值。
print(ebola.fillna(method='ffill').iloc[:, 0:5])

# 如果一列的开头缺少一个值，则该数据仍将丢失，因为没有以前的值可填充。

# 向后填充。
print(ebola.fillna(method='bfill').iloc[:, 0:5])

# 插值使用现有的值来填充缺失的值。
# 有很多方法可以填充缺失值，Pandas 中的插值线性地填充缺失值。
# 特别是，它将缺失值视为应该等距排列。
print(ebola.interpolate().iloc[:, 0:5])
