#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - box 图。

@Time: 2023/6/12
@Author: Lingchen
@Prescription: P160.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

box, ax = plt.subplots()

# x是可选的，但y必须是数字变量。
# sns.boxplot(data=tips, y='total_bill', ax=ax)
sns.boxplot(data=tips, x='time', y='total_bill', ax=ax)

ax.set_title('Box Plot of Total Bill by Time of Day')
ax.set_xlabel('Time of Day')
ax.set_ylabel('Total Bill')

plt.show()
