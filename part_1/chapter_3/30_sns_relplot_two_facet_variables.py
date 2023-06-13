#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 两个字变量的 图形。

@Time: 2023/6/13
@Author: Lingchen
@Prescription: P175.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 可以在此基础上，将两个分类变量合并到我们的分面图中。
# 其他分类变量可以传递到色调、风格等参数中。
colors = {
    'Yes': '#f1a340',       # 黄色。
    'No': '#998ec3'         # 紫色。
}

facets = sns.relplot(
    data=tips,
    x='total_bill',
    y='tip',
    hue='smoker',
    style='sex',
    kind='scatter',
    col='day',
    row='time',
    palette=colors,
    height=1.7          # 已调整以适应页面上的图形。
)

# 下面是为了让情节好看调整方面标题。
facets.set_titles(
    row_template='{row_name}',
    col_template='{col_name}'
)

sns.move_legend(
    facets,
    loc='lower center',
    bbox_to_anchor=(0.5, 1),
    ncol=2,                 # 数字图例列。
    title=None,             # 图例标题。
    frameon=False           # 删除图例周围的边框（即边框）。
)

facets.figure.set_tight_layout(True)

plt.show()
