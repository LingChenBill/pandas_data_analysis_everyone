#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
获取Pandas系列的唯一值计数和频率计数.

@Time: 2023/6/4
@Author: Lingchen
@Prescription: P72.
"""
import logging
import pandas as pd
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', sep='\t')
print(df.head())

# 使用 nunique(数字唯一) 计算序列中唯一值的数量
print(df.groupby('continent')['country'].nunique())

# 再看世界人口的年预期寿命
global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)

global_yearly_life_expectancy.plot()
plt.show()
