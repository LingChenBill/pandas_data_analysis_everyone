#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 创建 box 图形。

@Time: 2023/6/14
@Author: Lingchen
@Prescription: P198.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 方框图是使用 DataFrame.plot.Box() 函数创建的。
fig, ax = plt.subplots()
ax = tips.plot.box(ax=ax)
plt.show()
