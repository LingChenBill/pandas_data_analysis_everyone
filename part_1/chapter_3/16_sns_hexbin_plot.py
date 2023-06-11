#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 Hexbin 图。

@Time: 2023/6/11
@Author: Lingchen
@Prescription: P154.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 可以将 kind='hex' 的 jointplot 用于 hexbin 图。
hexbin = sns.jointplot(data=tips, x='total_bill', y='tip', kind='hex')

hexbin.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
hexbin.figure.suptitle('Hexbin Plot of Total Bill and Tip', y=1.03)

plt.show()
