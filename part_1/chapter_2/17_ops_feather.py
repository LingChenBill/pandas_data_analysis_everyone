#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
导出与导入到 feather 文件中。

@Time: 2023/6/8
@Author: Lingchen
@Prescription: P110.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')
print(scientists.head())

# 导出到 feather 文件中。
scientists.to_feather('../../output/scientists.feather')

# 导入 feather 文件。
sci_feather = pd.read_feather('../../output/scientists.feather')
print(sci_feather)
