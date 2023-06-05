#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
手动创建一个series.

@Time: 2023/6/5
@Author: Lingchen
@Prescription: P77.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

s = pd.Series(['banana', 42])
print(s)

# 手动将索引值分配给序列
s = pd.Series(
    data=['Wes McKinney', 'Creator of Pandas'],
    index=['Person', 'Who']
)
print(s)
