#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 violin 小提琴图形(配置颜色)。

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

violin, ax = plt.subplots()

sns.violinplot(
    data=tips,
    x='time',
    y='total_bill',
    hue='smoker',           # 根据 吸烟者 变量设置颜色。
    split=True,
    palette='viridis',      # 调色板指定色调的颜色。
    ax=ax
)

plt.show()
