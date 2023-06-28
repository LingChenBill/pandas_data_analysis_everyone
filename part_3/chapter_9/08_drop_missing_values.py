#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 去掉缺失值。

@Time: 2023/6/28
@Author: Lingchen
@Prescription: P372.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

ebola = pd.read_csv('../../data/country_timeseries.csv')
print(ebola.head())

# 处理缺失数据的最后一种方法是删除缺失数据的观测值或变量。
# 可以使用 .dropna() 方法删除丢失的数据，并为该方法指定控制数据删除方式的参数。
# 当缺少"any"或"all"数据时，是否删除行（或列）。
# thresh 参数允许您指定在删除行或列之前有多少非 NaN 值。
print(ebola.shape)

# 如果在 ebola 数据集中只保留完整的病例，我们只剩下一行数据。
ebola_dropna = ebola.dropna()
print(ebola_dropna.shape)

print(ebola_dropna)

print(ebola.columns)

# 具有"缺失值"的计算通常会返回缺失值，除非调用的函数或方法能够忽略其计算中的缺失值。
ebola['Cases_multiple'] = (
    ebola['Cases_Guinea']
    + ebola['Cases_Liberia']
    + ebola['Cases_SierraLeone']
)

print(ebola.head())

ebola_subset = ebola.loc[
    :,
    [
        'Cases_Guinea',
        'Cases_Liberia',
        'Cases_SierraLeone',
        'Cases_multiple'
    ]
]
print(ebola_subset.head(n=10))

# 跳过缺少的值默认为 True。
print(ebola['Cases_Guinea'].sum(skipna=True))

print(ebola['Cases_Guinea'].sum(skipna=False))
