#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 pairwise 成对的图形。

@Time: 2023/6/12
@Author: Lingchen
@Prescription: P164.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 当你的数据大多是数字时，可以使用 sns.pairplot() 来可视化所有的成对关系。
# 这个函数将在每对变量之间绘制散点图，并为单变量数据绘制直方图。
fig = sns.pairplot(data=tips)

fig.figure.suptitle('Pairwise Relationships of the Tips Data', y=1.03)

plt.show()
