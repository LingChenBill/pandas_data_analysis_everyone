#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
输出与导入数据到pickle文件中。

@Time: 2023/6/8
@Author: Lingchen
@Prescription: P105.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')
print(scientists.head())

names = scientists['Name']
print(names)

# 将 姓名 列保存到 pickle 文件中。
names.to_pickle('../../output/scientists_names_series.pickle')

# dataframe 也可保存到 pickle 中。
scientists.to_pickle('../../output/scientists_df.pickle')

# 读取 pickle 文件。
series_pickle = pd.read_pickle('../../output/scientists_names_series.pickle')
print(series_pickle)

df_pickle = pd.read_pickle('../../output/scientists_df.pickle')
print(df_pickle)
