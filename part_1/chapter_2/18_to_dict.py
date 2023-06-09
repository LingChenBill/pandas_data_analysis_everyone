#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
series 和 df 转换成 dict。

@Time: 2023/6/9
@Author: Lingchen
@Prescription: P113.
"""
import logging
import pandas as pd
import pprint

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')
print(scientists.head())

sci_sub_dict = scientists.head(2)
print(sci_sub_dict)

# df 转换成 dict。
sci_dict = sci_sub_dict.to_dict()
pprint.pprint(sci_dict)

# 从 dict 中读取数据成 df。
sci_dict_df = pd.DataFrame.from_dict(sci_dict)
print(sci_dict_df)
