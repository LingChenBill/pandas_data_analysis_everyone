#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 日期范围处理。

@Time: 2023/7/2
@Author: Lingchen
@Prescription: P383.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 并不是每个数据集都有固定的值频率。
# 例如，在 埃博拉 数据集中，没有对日期范围内的每一天进行观察。
ebola = pd.read_csv(
    '../../data/country_timeseries.csv',
    parse_dates=['Date']
)
print(ebola.iloc[:, :5])

# 此处，数据的 .head() 中缺少2015-01-01。
# 通常的做法是创建一个日期范围来 .reindex() 数据集。可以使用 date_range()。
head_range = pd.date_range(start='2014-12-31', end='2015-01-05')
print(head_range)

ebola_5 = ebola.head()

# 如果要将此日期范围设置为索引，则需要首先将日期设置为索引。
ebola_5.index = ebola_5['Date']

ebola_5 = ebola_5.reindex(head_range)

print(ebola_5.iloc[:, :5])

# 日期频率。'B' - 工作日
print(pd.date_range('2022-01-01', '2022-01-07', freq='B'))

# 可以采用刚刚创建的工作日范围，并添加一个偏移量，这样就可以包括其他每个工作日的数据，而不是每个工作日。
print(pd.date_range('2022-01-01', '2017-01-07', freq='2B'))

# 通过在基频之前加一个乘积来创建这种偏移。这种偏移也可以与其他基频组合。
# 可以指定2022年每个月的第一个星期四。
print(pd.date_range('2022-01-01', '2022-12-31', freq='WOM-1THU'))

# 指定每个月的第三个星期五。
print(pd.date_range('2022-01-01', '2022-12-31', freq='WOM-3FRI'))
