#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
创建一个DataFrame.

@Time: 2023/6/5
@Author: Lingchen
@Prescription: P78.
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
        "Age": [37, 61],
    }
)

print(scientists)

# 我们可以使用 columns 参数或指定列顺序。
# 如果要使用行索引的 name 列，我们可以使用 index 参数。
scientists = pd.DataFrame(
    {
        "Name": ["Rosaline Franklin", "William Gosset"],
        "Occupation": ["Chemist", "Statistician"],
        "Born": ["1920-07-25", "1876-06-13"],
        "Died": ["1958-04-16", "1937-10-16"],
        "Age": [37, 61],
    },
    index=["Rosaline Franklin", "William Gosset"],
    columns=['Occupation', 'Born', 'Died', 'Age'],
)

print(scientists)
