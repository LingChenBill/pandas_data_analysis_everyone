#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 列包含多个变量。

@Time: 2023/6/17
@Author: Lingchen
@Prescription: P241.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 有时数据集中的列可能代表多个变量。这种格式在处理运行 健康数据 时很常见。
ebola = pd.read_csv('../../data/country_timeseries.csv')
print(ebola.columns)

# 选取行和列。
print(ebola.iloc[:5, [0, 1, 2, 10]])

ebola_long = ebola.melt(id_vars=['Date', 'Day'])
print(ebola_long)

# 获取变量列, 访问字符串方法, 并根据分隔符拆分列。
variable_split = ebola_long.variable.str.split('_')
print(variable_split[:5])

# 类型。
print(type(variable_split))

# 第一个元素的类型。
print(type(variable_split[0]))

# 获取分隔的值。
status_values = variable_split.str.get(0)
country_values = variable_split.str.get(1)

print(status_values)
print(country_values)

# 将截取的列添加到 df 中。
ebola_long['status'] = status_values
ebola_long['country'] = country_values
print(ebola_long)
