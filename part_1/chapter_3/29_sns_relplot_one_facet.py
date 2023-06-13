#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 One Facet Variable 图形。

@Time: 2023/6/13
@Author: Lingchen
@Prescription: P173.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

anscombe = sns.load_dataset('anscombe', data_home='../../data/seaborn-data', cache=True)
print(anscombe)

anscombe_plot = sns.relplot(
    data=anscombe,
    x='x',
    y='y',
    kind='scatter',
    col='dataset',
    col_wrap=2,
    height=2,
    aspect=1.6          # 每个面的纵横比。
)

anscombe_plot.figure.set_tight_layout(True)

plt.show()
