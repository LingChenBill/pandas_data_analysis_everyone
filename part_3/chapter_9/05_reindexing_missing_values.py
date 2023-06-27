#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 重新索引（包含缺失值）。

@Time: 2023/6/27
@Author: Lingchen
@Prescription: P363.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 如果我们只想从第1.5节中的 Gapminder 数据图中查看2000年至2010年，
# 可以执行相同的分组操作，对数据进行子集化，然后重新索引。
gapminder = pd.read_csv('../../data/gapminder.tsv', sep='\t')
print(gapminder.head())

life_exp = gapminder.groupby(['year'])['lifeExp'].mean()
print(life_exp)

# 可以通过对数据进行子集设置来重新索引，并使用 .reindex() 方法。
y2000 = life_exp[life_exp.index > 2000]
print(y2000)

# 重新索引。
print(y2000.reindex(range(2000, 2010)))
