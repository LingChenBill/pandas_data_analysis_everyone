#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 创建kde图。

@Time: 2023/6/14
@Author: Lingchen
@Prescription: P194.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 可以使用DataFrame.plot.kde() 函数创建内核密度估计（密度）图。
fig, ax = plt.subplots()
tips['tip'].plot.kde(ax=ax)
plt.show()
