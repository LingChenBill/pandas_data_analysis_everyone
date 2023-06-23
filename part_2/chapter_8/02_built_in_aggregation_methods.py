#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 内置的聚合方法。

@Time: 2023/6/23
@Author: Lingchen
@Prescription: P318.
"""
import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', sep='\t')
print(df.head())

# 按大洲分组并描述每组。
continent_describe = df.groupby('continent')['lifeExp'].describe()
print(continent_describe)

# 当将函数传入 .agg() 时，只需要实际的函数对象，而不需要"调用"函数。
# 这就是为什么写 np.mean 而不是 np.mean()。

# 使用 np.mean() 按大洲计算平均预期寿命。
cont_le_agg = df.groupby('continent')['lifeExp'].agg(np.mean)
print(cont_le_agg)
