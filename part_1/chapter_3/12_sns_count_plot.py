#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 bar 图。

@Time: 2023/6/11
@Author: Lingchen
@Prescription: P147.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 条形图与直方图非常相似，但条形图可以用来计算离散变量，而不是将值合并以产生分布。
# Seaborn称之为计数图。
count, ax = plt.subplots()

# 我们可以使用 viridis 调色板来帮助区分颜色。
sns.countplot(data=tips, x='day', palette='viridis', ax=ax)

ax.set_title('Count of days')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Frequency')

plt.show()
