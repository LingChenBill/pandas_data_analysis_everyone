#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 创建 hexbin 图形。

@Time: 2023/6/14
@Author: Lingchen
@Prescription: P196.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

fig, ax = plt.subplots()
tips.plot.hexbin(x='total_bill', y='tip', ax=ax)
plt.show()

fig, ax = plt.subplots()
# 可以使用 gridsize 参数调整网格大小。
tips.plot.hexbin(
    x='total_bill', y='tip', gridsize=10, ax=ax
)
plt.show()
