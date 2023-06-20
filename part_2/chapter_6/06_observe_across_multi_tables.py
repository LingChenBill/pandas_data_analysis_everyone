#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 从不同的文件中加载数据，连接df。

@Time: 2023/6/20
@Author: Lingchen
@Prescription: P247.
"""
import logging
import pandas as pd
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 加载不同文件中的数据。
billboard_data_files = (
    Path(".").glob('../../data/billboard-by_week/billboard-*.csv')
)

# 文件排序。
billboard_data_files = sorted(list(billboard_data_files))
print(billboard_data_files)

billboard_data_files = list(billboard_data_files)

# 读取文件数据。
billboard01 = pd.read_csv(billboard_data_files[0])
billboard02 = pd.read_csv(billboard_data_files[1])
billboard03 = pd.read_csv(billboard_data_files[2])

print(billboard01)

print(billboard01.shape)
print(billboard02.shape)
print(billboard03.shape)

# 连接 df。
billboard = pd.concat([billboard01, billboard02, billboard03])
print(billboard.shape)

# 验证行数。
assert(
    billboard01.shape[0]
    + billboard02.shape[0]
    + billboard03.shape[0]
    == billboard.shape[0]
)
