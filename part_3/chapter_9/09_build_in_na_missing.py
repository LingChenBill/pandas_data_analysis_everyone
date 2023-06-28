#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 内置的缺失值处理。

@Time: 2023/6/28
@Author: Lingchen
@Prescription: P375.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.DataFrame(
    {
        "Name": ["Rosaline Franklin", "William Gosset"],
        "Occupation": ["Chemist", "Statistician"],
        "Born": ["1920-07-25", "1876-06-13"],
        "Died": ["1958-04-16", "1937-10-16"],
        "Age": [37, 61]
    }
)
print(scientists)

print(scientists.dtypes)

# 由于 pd.NA 仍处于试验阶段，最好在官方文档中跟进其行为。
scientists.loc[1, 'Name'] = pd.NA
scientists.loc[1, 'Age'] = pd.NA

print(scientists)
print(scientists.dtypes)
