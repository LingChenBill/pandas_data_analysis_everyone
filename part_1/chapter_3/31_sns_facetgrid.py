#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 创建 面网格 facet grid。

@Time: 2023/6/13
@Author: Lingchen
@Prescription: P.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 创建一个FacetGrid，它知道在哪个变量上进行facet，
# 然后为每个facet提供单独的绘图代码。

facet = sns.FacetGrid(
    tips,
    col='time'
)

# 对于时间上的每个值，绘制总账单的直方图。
facet.map(sns.histplot, 'total_bill')

plt.show()
