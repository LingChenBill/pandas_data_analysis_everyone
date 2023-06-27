#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 统计缺失值。

@Time: 2023/6/27
@Author: Lingchen
@Prescription: P365.
"""
import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 查找并计数丢失的数据。
ebola = pd.read_csv('../../data/country_timeseries.csv')
# 计算非缺失值的数量。
print(ebola.count())

# 从总行数中减去未丢失的行数。
num_rows = ebola.shape[0]
num_missing = num_rows - ebola.count()
print(num_missing)

# 如果要计算数据中丢失值的总数，或者计算某一列的丢失值的数量，
# 可以将 numpy 中的 count_nonzero() 函数与 .isnull() 方法结合使用。
print(np.count_nonzero(ebola.isnull()))

print(np.count_nonzero(ebola['Cases_Guinea'].isnull()))

# Cases_Guinea 列中的值计数。
cnts = ebola['Cases_Guinea'].value_counts(dropna=False)
print(cnts)

# 选择序列中索引为 NaN 值的值。
print(cnts.loc[pd.isnull(cnts.index)])

# 检查值是否丢失，并对结果进行汇总。
print(ebola['Cases_Guinea'].isnull().sum())
