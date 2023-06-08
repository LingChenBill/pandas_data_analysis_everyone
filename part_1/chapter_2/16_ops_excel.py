#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
导出与导入excel。

@Time: 2023/6/8
@Author: Lingchen
@Prescription: P109.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')
print(scientists.head())

names = scientists['Name']
print(names)

# Series 数据结构没有显式的 .to_excel() 方法。
# 如果您有一个需要导出到 excel 文件的 Series，一个选项是将该Series转换为单列 DataFrame。
names_df = names.to_frame()
print(names_df)

names_df.to_excel('../../output/scientists_names_series_df.xls', engine='openpyxl')

# 保存 df 到 excel。
scientists.to_excel(
    '../../output/scientists_df.xlsx',
    sheet_name='scientists',
    index=False,
)
