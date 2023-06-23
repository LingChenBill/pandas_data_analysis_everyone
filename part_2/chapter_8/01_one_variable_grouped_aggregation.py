#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 基于一个变量的分组聚合。

@Time: 2023/6/23
@Author: Lingchen
@Prescription: P316.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', sep='\t')
print(df.head())

# 计算每年的平均预期寿命。
avg_life_exp_by_year = df.groupby('year')['lifeExp'].mean()
print(avg_life_exp_by_year)

# Groupby 语句可以被认为是为列的每个唯一值 (或列中的唯一对) 创建一个子集。
# 获取 year 列中的唯一值。
years = df.year.unique()
print(years)

# 获取某一年份的数据。
y1952 = df.loc[df.year == 1952, :]
print(y1952)

# 可以对子集数据执行函数。这里我们取 lifeExp 值的平均值。
y1952_mean = y1952['lifeExp'].mean()
print(y1952_mean)
