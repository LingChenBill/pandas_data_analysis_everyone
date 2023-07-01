#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 日期计算和日期增量。

@Time: 2023/7/1
@Author: Lingchen
@Prescription: P432.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

ebola = pd.read_csv('../../data/country_timeseries.csv', parse_dates=['Date'])
print(ebola.head())
# print(ebola.info())

# 我们的 ebola 数据集包括一个名为 Day 的列，它指示一个国家爆发埃博拉疫情的天数。
# 我们可以使用日期算术重新创建这个列。
print(ebola.iloc[-5:, :5])

# 疫情爆发的第一天（本数据集中最早的日期）是2015-03-22。
# 因此，如果想计算疫情爆发的天数，可以使用该列的 .min() 方法从每个日期中减去这个日期。
ebola['date_dt'] = pd.to_datetime(ebola['Date'])
# print(ebola.iloc[-5:, :5])

# 查看日期的最小值。
print(ebola['date_dt'].min())

ebola['outbreak_d'] = ebola['date_dt'] - ebola['date_dt'].min()
print(ebola[['Date', 'date_dt', 'Day', 'outbreak_d']])

# 当进行这种日期计算时，实际上最终得到了一个 timedelta 对象。
print(ebola.info())
