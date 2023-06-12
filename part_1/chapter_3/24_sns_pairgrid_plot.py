#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 pair grid 图形。

@Time: 2023/6/12
@Author: Lingchen
@Prescription: P167.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 创建一个PairGrid，以不同的比例绘制对角线。
pair_grid = sns.PairGrid(tips, diag_sharey=False)

# 设置一个单独的函数来绘制上、下和对角线函数需要返回一个轴，而不是一个数字。

pair_grid = pair_grid.map_upper(sns.regplot)
pair_grid = pair_grid.map_lower(sns.kdeplot)
pair_grid = pair_grid.map_diag(sns.histplot)

plt.show()
