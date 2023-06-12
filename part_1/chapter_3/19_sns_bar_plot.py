#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 Bar 图。

@Time: 2023/6/12
@Author: Lingchen
@Prescription: P159.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

bar, ax = plt.subplots()

# 绘制每个时间值的平均总账单, 使用 numpy 计算平均值。
sns.barplot(data=tips, x='time', y='total_bill', estimator=np.mean, ax=ax)

ax.set_title('Bar Plot of Average Total Bill for Time of Day')
ax.set_xlabel('Time of Day')
ax.set_ylabel('Average Total Bill')

plt.show()
