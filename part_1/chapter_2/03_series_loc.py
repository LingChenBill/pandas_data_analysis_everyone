#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
从DataFrame中获取一个series.

@Time: 2023/6/5
@Author: Lingchen
@Prescription: P80.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists_df = pd.DataFrame(
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

print(scientists_df)

# 通过行索引值来选取行。
first_row = scientists_df.loc['William Gosset']
print(type(first_row))

# series 打印时， 索引被打印为第一个“列”，值被打印为第二个“栏”
print(first_row)

print(first_row.index)
print(first_row.values)

print(first_row.keys())

# 使用属性获取第一个索引
print(first_row.index[0])

# 使用方法获取第一个索引
print(first_row.keys()[0])
