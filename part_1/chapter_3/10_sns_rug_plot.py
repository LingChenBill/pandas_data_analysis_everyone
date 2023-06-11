#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - Rug 绘图。

@Time: 2023/6/11
@Author: Lingchen
@Prescription: P143.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

rug, ax = plt.subplots()

# 在我们创建的坐标轴上绘制两个东西。
# Rug图是变量分布的一维表示。
# 它们通常与其他图一起使用，以增强可视化效果。显示了底部覆盖有密度图和地毯图的直方图。
sns.rugplot(data=tips, x='total_bill', ax=ax)
sns.histplot(data=tips, x='total_bill', ax=ax)

ax.set_title('Rug Plot and Histogram of Total Bill')
ax.set_xlabel('Total Bill')

plt.show()
