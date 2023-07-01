#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 提交日期数据部分。

@Time: 2023/7/1
@Author: Lingchen
@Prescription: P428.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

ebola = pd.read_csv('../../data/country_timeseries.csv')

# 现在有了datetime对象，我们可以提取日期的各个部分，例如年、月或日。
d = pd.to_datetime('2021-12-14')
print(d)

# 如果传入一个字符串，就会得到一个时间戳。
print(type(d))

# 现在有了一个合适的日期时间，我们可以访问各种日期组件作为属性。
print(d.year)

print(d.month)

print(d.day)

print(ebola.info())

# 通过使用 .dt.accessor 访问 datetime 方法，
# 可以在这里对 datetime 对象执行类似的操作。
ebola['date_dt'] = pd.to_datetime(ebola['Date'])

print(ebola[['Date', 'date_dt']])

# 可以根据日期列创建新的年份列。
ebola['year'] = ebola['date_dt'].dt.year
print(ebola[['Date', 'date_dt', 'year']])

ebola = ebola.assign(
    month=ebola['date_dt'].dt.month,
    day=ebola['date_dt'].dt.day,
)
print(ebola[['Date', 'date_dt', 'year', 'month', 'day']])

print(ebola.info())
