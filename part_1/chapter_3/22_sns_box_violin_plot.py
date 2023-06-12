#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 box 和 violin 图形。

@Time: 2023/6/12
@Author: Lingchen
@Prescription: P163.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 创建两个子块的图形。
box_violin, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

sns.boxplot(data=tips, x='time', y='total_bill', ax=ax1)
sns.violinplot(data=tips, x='time', y='total_bill', ax=ax2)

ax1.set_title('Box Plot')
ax1.set_xlabel('Time of day')
ax1.set_ylabel('Total Bill')

ax2.set_title('Violin Plot')
ax2.set_xlabel('Time of day')
ax2.set_ylabel('Total Bill')

box_violin.suptitle('Comparison of Box Plot with Violin Plot')

# 将图形隔开，这样标签就不会重叠。
box_violin.set_tight_layout(True)

plt.show()
