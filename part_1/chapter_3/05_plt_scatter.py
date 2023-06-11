#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
绘图-散点图。

@Time: 2023/6/11
@Author: Lingchen
@Prescription: P134.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)

# 创建一个散点图。
axes1.scatter(data=tips, x='total_bill', y='tip')

axes1.set_title('Scatter plot of Total Bill vs Tip')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')

plt.show()
