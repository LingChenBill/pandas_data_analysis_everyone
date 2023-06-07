#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
添加另外的 columns (新增转换的日期格式的列).

@Time: 2023/6/7
@Author: Lingchen
@Prescription: P95.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')
print(scientists.dtypes)
print(scientists['Born'])

# 将“出生”列格式化为日期时间。
born_datatime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
print(born_datatime)

print(scientists['Died'])
died_datatime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
print(died_datatime)

# 我们可以创建一组新的列，其中包含对象（字符串）日期的 datetime 表示。
# 下面的示例使用python的多重赋值语法。
scientists['born_dt'], scientists['died_dt'] = (
    born_datatime,
    died_datatime
)
print(scientists.head())

print(scientists.shape)

print(scientists.dtypes)
