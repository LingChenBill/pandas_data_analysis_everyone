#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 joint 图。

@Time: 2023/6/12
@Author: Lingchen
@Prescription: P159.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

kde2d = sns.jointplot(data=tips, x='total_bill', y='tip', kind='kde')

kde2d.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
kde2d.fig.suptitle('2D KDE Plot of Total Bill and Tip', y=1.03)

plt.show()
