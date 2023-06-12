#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 散点图（大小和形状）。

@Time: 2023/6/12
@Author: Lingchen
@Prescription: P172.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

fig, ax = plt.subplots()

sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    hue='time',
    size='size',
    palette='viridis',
    ax=ax
)

plt.show()
