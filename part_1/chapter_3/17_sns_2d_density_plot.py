#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 2d Density 密度图。

@Time: 2023/6/12
@Author: Lingchen
@Prescription: P156.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

kde, ax = plt.subplots()

# 阴影将填充轮廓。
# sns.kdeplot(data=tips, x='total_bill', y='tip', ax=ax)
sns.kdeplot(data=tips, x='total_bill', y='tip', shade=True, ax=ax)

ax.set_title('Kernel Density Plot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

plt.show()
