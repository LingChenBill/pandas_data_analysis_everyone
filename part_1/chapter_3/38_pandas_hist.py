#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 创建直方图。

@Time: 2023/6/14
@Author: Lingchen
@Prescription: P194.
"""
import logging
import matplotlib.pyplot as plt
import seaborn as sns

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 在列上绘图。
fig, ax = plt.subplots()
tips['total_bill'].plot.hist(ax=ax)

plt.show()

# 在 df 上
# 设置 alpha 通道透明度以透视重叠的条形图
fig, ax = plt.subplots()
tips[['total_bill', 'tip']].plot.hist(alpha=0.5, bins=20, ax=ax)

plt.show()
