#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
dict 转换成 json 形式。

@Time: 2023/6/9
@Author: Lingchen
@Prescription: P115.
"""
import logging
import pandas as pd
import pprint

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')
print(scientists.head())

born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')

scientists = scientists.assign(
    born_dt=born_datetime,
    died_dt=died_datetime
)

sci_sub_dict = scientists.head(2)
print(sci_sub_dict)

# 将 df 转换成 json。 indent = 2 打印时显示更友好。
sci_json = sci_sub_dict.to_json(
    orient='records',
    indent=2,
    date_format='iso'
)
pprint.pprint(sci_json)

# 从 json 数据中拷贝数据到 df 中。
sci_json_df = pd.read_json(
    ('[\n'
     '  {\n'
     '    "Name":"Rosaline Franklin",\n'
     '    "Born":"1920-07-25",\n'
     '    "Died":"1958-04-16",\n'
     '    "Age":37,\n'
     '    "Occupation":"Chemist",\n'
     '    "born_dt":"1920-07-25T00:00:00.000Z",\n'
     '    "died_dt":"1958-04-16T00:00:00.000Z"\n'
     '  },\n'
     '  {\n'
     '    "Name":"William Gosset",\n'
     '    "Born":"1876-06-13",\n'
     '    "Died":"1937-10-16",\n'
     '    "Age":61,\n'
     '    "Occupation":"Statistician",\n'
     '    "born_dt":"1876-06-13T00:00:00.000Z",\n'
     '    "died_dt":"1937-10-16T00:00:00.000Z"\n'
     '  }\n'
     ']'),
    orient='records'
)

print(sci_json_df)
print(sci_json_df.dtypes)

# 若要时间列显示成datetime形式, 则要进行时间转换。
sci_json_df['died_dt_json'] = pd.to_datetime(sci_json_df['died_dt'])
print(sci_json_df)

print(sci_json_df.dtypes)
