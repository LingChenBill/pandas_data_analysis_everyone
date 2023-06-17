#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 保持多列固定。

@Time: 2023/6/17
@Author: Lingchen
@Prescription: P239.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

billboard = pd.read_csv('../../data/billboard.csv')
print(billboard.head())

# 不是每个数据集都有一列可以在取消透视其余列时保持静止。
# 查看前几行和几列。
print(billboard.iloc[0:5, 0:16])

# 如果您想创建每周评级的分面图，则分面变量需要是数据帧中的一列。
# 使用列表引用多个变量。
billboard_long = billboard.melt(
    id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
    var_name='week',
    value_name='rating'
)

print(billboard_long)
