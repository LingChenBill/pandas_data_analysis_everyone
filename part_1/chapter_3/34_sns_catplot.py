#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 创建 catplot 图形。

@Time: 2023/6/13
@Author: Lingchen
@Prescription: P183.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 如果您不希望所有色调元素重叠（即，您希望这种行为出现在散点图中，而不是小提琴图中），
# 您可以使用sns.catplot() 函数。
facet = sns.catplot(
    x='day',
    y='total_bill',
    hue='sex',
    data=tips,
    row='smoker',
    col='time',
    kind = 'violin'
    # kind='swarm'
)

plt.show()

