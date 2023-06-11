#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制joint图。

@Time: 2023/6/11
@Author: Lingchen
@Prescription: P152.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 联合绘图为我们创造了图形和轴线。
joint = sns.jointplot(data=tips, x='total_bill', y='tip')

joint.set_axis_labels(xlabel='Total Bill', ylabel='Tip')

joint.figure.suptitle('Joint Plot of Total Bill and Tip', y=1.03)

plt.show()
