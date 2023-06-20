#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 利用列表推导式来加载多个文件的数据。

@Time: 2023/6/20
@Author: Lingchen
@Prescription: P253.
"""
import logging
import pandas as pd
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

billboard_data_files = (
    Path('.').glob('../../data/billboard-by_week/billboard-*.csv')
)

list_billboard_df = []
for csv_filename in billboard_data_files:
    df = pd.read_csv(csv_filename)
    list_billboard_df.append(df)

print(list_billboard_df)

# glob 是一个生成器，前面已经使用完了，再次使用 billboard_data_files 时，要重新生成一次。
billboard_data_files = (
    Path('.').glob('../../data/billboard-by_week/billboard-*.csv')
)

# 使用列表推导式来加载数据。
billboard_dfs = [pd.read_csv(data) for data in billboard_data_files]
print(billboard_dfs)

# 打印 billboard_dfs 的类型。
print(type(billboard_dfs))

print(len(billboard_dfs))

# 连接 df 数据。
billboard_concat_comp = pd.concat(billboard_dfs)
print(billboard_concat_comp)
