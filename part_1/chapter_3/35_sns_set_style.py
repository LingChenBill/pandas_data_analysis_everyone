#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制图形的样式。

@Time: 2023/6/13
@Author: Lingchen
@Prescription: P185.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

fig, ax = plt.subplots()
sns.violinplot(
    data=tips,
    x='time',
    y='total_bill',
    hue='sex',
    split=True,
    ax=ax
)

# 默认样式。
# sns.set_style('whitegrid')

plt.show()

# 如果使用sns.set_style()，请删除带行+缩进的。
# with sns.axes_style('darkgrid'):
#
#     fig, ax = plt.subplots()
#     sns.violinplot(
#         data=tips, x='time', y='total_bill', hue='sex', split=True, ax=ax
#     )

sns.set_style('darkgrid')
fig, ax = plt.subplots()
sns.violinplot(
    data=tips, x='time', y='total_bill', hue='sex', split=True, ax=ax
)
plt.show()
