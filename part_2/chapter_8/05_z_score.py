#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - z-score 计算。

@Time: 2023/6/24
@Author: Lingchen
@Prescription: P329.
"""
import logging
import pandas as pd
from scipy.stats import zscore

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', sep='\t')
print(df.head())

# z-score 确定了数据平均值的标准差数量。
# 它将我们的数据集中在0左右，标准差为1。
# 这项技术标准化了我们的数据，使更容易将不同单位的不同变量相互比较。


def my_zscore(x):
    """
    计算所提供数据的z分数。
    :param x: 一个向量或一系列值。
    :return: z-score
    """
    return (x - x.mean()) / x.std()


transform_z = df.groupby('year')['lifeExp'].transform(my_zscore)
print(transform_z)

print(df.shape)

# 注意转换中的值数量。
print(transform_z.shape)

# scipy 库有自己的 zscore() 函数。
# 让在 .groupby().transform() 中使用它的 zscore() 函数，
# 并将其与不使用 .groupy() 时的情况进行比较。
sp_z_grouped = df.groupby('year')['lifeExp'].transform(zscore)

# 计算一个未分组的 zscore。
sp_z_nogroup = zscore(df['lifeExp'])

print(transform_z.head())

print(sp_z_grouped.head())

# 分组结果相似。但是，当我们在 .groupby() 之外计算 z-score 时，
# 得到的是整个数据集的 z-score，而不是按组划分的。
print(sp_z_nogroup[:5])
