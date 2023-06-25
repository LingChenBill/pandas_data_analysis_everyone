#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 同时多个函数。

@Time: 2023/6/24
@Author: Lingchen
@Prescription: P325.
"""
import logging
import pandas as pd
import numpy as np
from pyarrow.interchange import column

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', '\t')
print(df.head())

# 当想计算多个聚合函数时，我们可以将单个函数作为 Python 列表传递到 .agg() 或 .aggregate() 中。
gdf = (
    df.groupby('year')['lifeExp']
    .agg([np.count_nonzero, np.mean, np.std])
)

print(gdf)

# 在分组的 DataFrame 上指定 dict 时，键是 DataFrame 的列，值是聚合计算中使用的函数。
# 在数据帧上使用字典标记不同的列, 对于每年，计算平均 lifeExp 中值 pop 和中值 gdpPercap。
gdf_dict = df.groupby('year').agg(
    {
        'lifeExp': 'mean',
        'pop': 'median',
        'gdpPercap': 'median'
    }
)

print(gdf_dict)

# 要在分组序列计算的输出中包含用户定义的列名，需要在事实之后重命名这些列。
gdf = (
    df.groupby('year')['lifeExp']
    .agg(
        [
            np.count_nonzero,
            np.mean,
            np.std
        ],
    )
    .rename(
        columns={
            'count_nonzero': 'count',
            'mean': 'avg',
            'std': 'std_dev'
        }
    )
    .reset_index()
)

print(gdf)
