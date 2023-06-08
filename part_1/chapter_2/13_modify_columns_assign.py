#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
使用 assign 方法来修改列 columns。

@Time: 2023/6/8
@Author: Lingchen
@Prescription: P101.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')
print(scientists.head())

born_datatime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
died_datatime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')

scientists['born_dt'], scientists['died_dt'] = (
    born_datatime,
    died_datatime
)

# 使用日期时间算术重新计算“实际”年龄。
scientists['age_days'] = (
        scientists['died_dt'] - scientists['born_dt']
)
print(scientists)

# 等号左侧的新列
# 如何计算等号右边的值
# scientists = scientists.assign(
#     age_days_assign=scientists['died_dt'] - scientists['born_dt'],
#     age_year_assign=scientists['age_days'].astype('timedelta64[Y]')
# )
# print(scientists.head())

# 使用 lambda 方式来赋值新列。
scientists = scientists.assign(
    age_days_assign=scientists['died_dt'] - scientists['born_dt'],
    age_year_assign=lambda df_: df_['age_days_assign'].astype('timedelta64[Y]')
)

print(scientists.columns)
print(scientists[['born_dt', 'died_dt',
                 'age_days', 'age_days_assign', 'age_year_assign']])
