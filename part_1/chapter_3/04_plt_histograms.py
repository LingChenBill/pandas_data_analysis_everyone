#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
统计图形-直方图。

@Time: 2023/6/11
@Author: Lingchen
@Prescription: P131.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips)

# 创建一个图形。
fig = plt.figure()

# 子绘图有1行1列，绘图位置1。
axes1 = fig.add_subplot(1, 1, 1)

# 绘制直方图。
axes1.hist(data=tips, x='total_bill', bins=10)

# 添加标签。
axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Total Bill')

plt.show()
