#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 violin 图形(小提琴图)。

@Time: 2023/6/12
@Author: Lingchen
@Prescription: P162.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 小提琴图可以显示与盒图相同的值，但将“盒”绘制为内核密度估计。
# 这有助于保留有关数据的更多视觉信息，因为仅绘制摘要统计数据可能会产生误导。
violin, ax = plt.subplots()

sns.violinplot(data=tips, x='time', y='total_bill', ax=ax)

ax.set_title('Violin plot of total bill by time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')

plt.show()
