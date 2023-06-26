#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 使用复数的索引来进行 Groupby 工作。

@Time: 2023/6/26
@Author: Lingchen
@Prescription: P297.
"""
import logging
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

intv_df = pd.read_csv('../../data/epi_sim.zip')
print(intv_df)

# 让计算每次复制的干预次数、干预时间和治疗值。
# 在这里，任意计算 ig_type。只需要一个值来计算各组的观察次数。
count_only = (
    intv_df
    .groupby(['rep', 'intervened', 'tr'])
    ['ig_type']
    .count()
)
print(count_only)

print(type(count_only))

# 结果采用多索引序列的形式。
# 如果想执行另一个 .groupby（）操作，必须传入 levels 参数以引用多索引级别。
# 这里，传入[0，1，2]用于第一、第二和第三索引级别。
count_mean = count_only.groupby(level=[0, 1, 2]).mean()
print(count_mean)

# 复合式写法。
count_mean = (
    intv_df
    .groupby(['rep', 'intervened', 'tr'])['ig_type']
    .count()
    .groupby(level=[0, 1, 2])
    .mean()
)
print(count_mean)

# 展示结果。
# 分组的累积计数。图表显示，其中一个复制没有在我们的模拟中运行。
fig = sns.lmplot(
    data=count_mean.reset_index(),
    x='intervened',
    y='ig_type',
    hue='rep',
    col='tr',
    fit_reg=False,
    palette='viridis'
)

plt.show()

# 还可以传入级别的字符串，使我们的代码可读性更强。
# 将使用 .cumsum() 来计算累积和，而不是查看.mean()。
cumulative_count = (
    intv_df
    .groupby(['rep', 'intervened', 'tr'])
    ['ig_type']
    .count()
    .groupby(level=['rep'])
    .cumsum()
    .reset_index()
)

fig = sns.lmplot(
    data=cumulative_count,
    x='intervened',
    y='ig_type',
    hue='rep',
    col='tr',
    fit_reg=False,
    palette='viridis'
)

plt.show()
