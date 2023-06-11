#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns- 分配图。

@Time: 2023/6/11
@Author: Lingchen
@Prescription: P144.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 更新的 sns.displot() 函数允许我们将许多单变量图组合成一个图。
# FacetGrid 对象为我们创建图形和轴。
fig = sns.displot(data=tips, x='total_bill', kde=True, rug=True)

fig.set_axis_labels(x_var='Total Bill', y_var='Count')
fig.figure.suptitle('Distribution of Total Bill')

plt.show()
