#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
seaborn 密集绘图-kdeplot。

@Time: 2023/6/11
@Author: Lingchen
@Prescription: P142.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)

den, ax = plt.subplots()

# 密度图是可视化单变量分布的另一种方式。
# 本质上，密度图是通过绘制以每个数据点为中心的正态分布，然后平滑重叠的图，使曲线下的面积为1来创建的。
sns.kdeplot(data=tips, x='total_bill', ax=ax)

ax.set_title('Total Bill Density')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Unit Probability')

plt.show()
