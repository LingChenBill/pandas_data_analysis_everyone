#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 使用 loop 来加载多个文件。

@Time: 2023/6/20
@Author: Lingchen
@Prescription: P250.
"""
import logging
import pandas as pd
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

billboard_data_files = (
    Path('.').glob('../../data/billboard-by_week/billboard-*.csv')
)

# 创建一个空的列表。
list_billboard_df = []

for csv_filename in billboard_data_files:
    print(csv_filename)
    df = pd.read_csv(csv_filename)

    # 将 df 添加到 list 中。
    list_billboard_df.append(df)

# 打印 df 的长度。
print(len(list_billboard_df))

# df 第一个元素的类型。
print(type(list_billboard_df[0]))

print(list_billboard_df[0])

billboard_loop_concat = pd.concat(list_billboard_df)
print(billboard_loop_concat.shape)
