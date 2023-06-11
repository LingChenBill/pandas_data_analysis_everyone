#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
seaborn 来绘制直方图。

@Time: 2023/6/11
@Author: Lingchen
@Prescription: P140.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)

# 设置为 paper 打印优化的默认seaborn上下文， 默认为 notebook
sns.set_context('paper')

# 子块功能是创建单独的地物对象和在图形中添加单独的子图形（轴）。
hist, ax = plt.subplots()

# 使用 seaborn 在轴上绘制直方图。
sns.histplot(data=tips, x='total_bill', ax=ax)

ax.set_title('Total Bill Histogram')

plt.show()
