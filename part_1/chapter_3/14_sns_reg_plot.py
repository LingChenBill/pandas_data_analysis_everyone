#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 reg 回归散点图。

@Time: 2023/6/11
@Author: Lingchen
@Prescription: P149.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 可以使用 sns.regplot() 创建散点图并绘制回归线。
reg, ax = plt.subplots()

sns.regplot(data=tips, x='total_bill', y='tip', ax=ax)

ax.set_title('Regression Plot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

plt.show()

# 类似的函数 sns.lmplot() 也可以创建散点图。
# 在内部，sns.lmplot() 调用 sns.regplot()。
fig = sns.lmplot(data=tips, x='total_bill', y='tip')

plt.show()
