#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 用户输出值（包含缺失值）

@Time: 2023/6/27
@Author: Lingchen
@Prescription: P362.
"""
import logging
import pandas as pd
from numpy import nan, NaN

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 将创建缺少值的自己的数据。NaN 值对 Series 和 DataFrame 对象都有效。
num_legs = pd.Series(
    {
        'goat': 4,
        'amoeba': nan
    }
)
print(num_legs)

scientists = pd.DataFrame(
    {
        "Name": ["Rosaline Franklin", "William Gosset"],
        "Occupation": ["Chemist", "Statistician"],
        "Born": ["1920-07-25", "1876-06-13"],
        "Died": ["1958-04-16", "1937-10-16"],
        "missing": [NaN, nan]
    }
)
print(scientists)

# 注意到丢失列的数据类型将是 float64。这是因为 numpy 中缺少的 NaN 值是浮点值。
print(scientists.dtypes)

# 也可以直接为数据帧分配一列缺少的值。
scientists = pd.DataFrame(
    {
        "Name": ["Rosaline Franklin", "William Gosset"],
        "Occupation": ["Chemist", "Statistician"],
        "Born": ["1920-07-25", "1876-06-13"],
        "Died": ["1958-04-16", "1937-10-16"],
    }
)
print(scientists)

scientists['missing'] = nan
print(scientists)
