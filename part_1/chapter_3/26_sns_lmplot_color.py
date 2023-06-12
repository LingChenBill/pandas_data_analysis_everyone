#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 implot 颜色图形。

@Time: 2023/6/12
@Author: Lingchen
@Prescription: P169.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

scatter = sns.lmplot(
    data=tips,
    x='total_bill',
    y='tip',
    hue='smoker',
    fit_reg=False,
    palette='viridis'
)

plt.show()
