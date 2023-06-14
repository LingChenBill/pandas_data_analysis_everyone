#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 创建散点图。

@Time: 2023/6/14
@Author: Lingchen
@Prescription: P195.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 散点图是使用 DataFrame.plot.scatter() 函数创建的。
fig, ax = plt.subplots()
tips.plot.scatter(x='total_bill', y='tip', ax=ax)
plt.show()
