#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 创建 facet grid 带有row标签的图形。

@Time: 2023/6/13
@Author: Lingchen
@Prescription: P181.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 可以用facet做的另一件事是让一个变量在x轴上分面，另一个变量则在y轴上分面的。
# 通过传递一个row参数来实现这一点。
facet = sns.FacetGrid(
    tips,
    col='time',
    row='smoker',
    hue='sex',
    palette='viridis'
)

facet.map(plt.scatter, 'total_bill', 'tip')

plt.show()
