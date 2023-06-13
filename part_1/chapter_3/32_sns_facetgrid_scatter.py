#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 创建 facet grid 的散点图形。

@Time: 2023/6/13
@Author: Lingchen
@Prescription: P179.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

facet = sns.FacetGrid(
    tips,
    col='day',
    hue='sex',
    palette='viridis'
)

facet.map(plt.scatter, 'total_bill', 'tip')
facet.add_legend()

plt.show()
