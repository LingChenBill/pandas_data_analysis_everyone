#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 加载包含有日期的数据。

@Time: 2023/7/1
@Author: Lingchen
@Prescription: P426.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# read_csv() 函数有很多参数，
# 例如 parse_dates、inher_datetime_format、keep_date_col、date_parser、dayfirst 和 cache_dates。

# Date : object
ebola = pd.read_csv('../../data/country_timeseries.csv')
print(ebola.info())

# Date : datetime64[ns]
ebola_date = pd.read_csv('../../data/country_timeseries.csv', parse_dates=['Date'])
print(ebola_date.info())
