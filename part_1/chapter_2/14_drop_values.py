#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
删除列。

@Time: 2023/6/8
@Author: Lingchen
@Prescription: P104.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')

born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')

scientists = scientists.assign(
    born_dt=born_datetime,
    died_dt=died_datetime,
    age_days=lambda df_: df_['died_dt'] - df_['born_dt'],
    age_years=lambda df_: df_['age_days'].astype('timedelta64[Y]'),
)
print(scientists.head())

print(scientists.columns)

# 删除列。
scientists_dropped = scientists.drop(['Age'], axis='columns')
print(scientists_dropped.columns)
print(scientists_dropped)
