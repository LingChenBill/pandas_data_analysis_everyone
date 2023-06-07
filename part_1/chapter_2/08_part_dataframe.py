#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
DataFrame的索引，列，值操作。

@Time: 2023/6/7
@Author: Lingchen
@Prescription: P92.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')

# 输出 index。
print(scientists.index)

# 输出 columns。
print(scientists.columns)

# 输出 值。
# 当您不需要所有的行索引标签信息，而只需要数据的基本 numpy 表示形式时，.values就派上了用场。
print(scientists.values)
