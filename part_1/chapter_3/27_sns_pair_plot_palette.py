#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 pair 颜色图形。

@Time: 2023/6/12
@Author: Lingchen
@Prescription: P171.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

fig = sns.pairplot(
    data=tips,
    hue='time',
    palette='viridis',
    height=2,                   # 刻面高度使整个图形变小。
)

plt.show()
