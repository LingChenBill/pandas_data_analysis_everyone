#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 一步分拆和合并。

@Time: 2023/6/17
@Author: Lingchen
@Prescription: P245.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

ebola = pd.read_csv('../../data/country_timeseries.csv')

ebola_long = ebola.melt(id_vars=['Date', 'Day'])
print(ebola_long.head())

# 通过 _ 将列拆分为使用 expand 的数据帧。
# 有一个名为 expand 的参数默认为False，
# 但当将其设置为 True 时，它将返回一个 DataFrame，其中拆分的每个结果都在一个单独的列中，而不是一系列列表容器中。
variable_split = ebola_long.variable.str.split('_', expand=True)
print(variable_split)

# 将生成的 df 合并到 原有的 df 中。
ebola_long[['status', 'country']] = variable_split
print(ebola_long)
