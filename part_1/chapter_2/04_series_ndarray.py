#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
许多在ndarray上操作的方法和函数也将在Series上操作。

@Time: 2023/6/5
@Author: Lingchen
@Prescription: P82.
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
    },
    index=["Rosaline Franklin", "William Gosset"],
    columns=['Occupation', 'Born', 'Died', 'Age'],
)

print(scientists)

# 获取 Age 列。
ages = scientists['Age']
print(ages)

print(ages.mean())

print(ages.min())

print(ages.max())

print(ages.std())
