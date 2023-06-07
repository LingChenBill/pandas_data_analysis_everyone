#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
带有公共索引标签的矢量。

@Time: 2023/6/7
@Author: Lingchen
@Prescription: P90.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')
ages = scientists['Age']
print(ages)

# 按 index 降序排列输出。
rev_ages = ages.sort_index(ascending=False)
print(rev_ages)

# 引用输出以显示索引标签对齐方式。
print(ages * 2)

# 注意，即使向量反转，我们如何获得相同的值。
print(ages + rev_ages)
print(rev_ages + ages)
