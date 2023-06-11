#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
绘制 box plot 箱线图.

@Time: 2023/6/11
@Author: Lingchen
@Prescription: P134.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)

boxplot = plt.figure()
axes1 = boxplot.add_subplot(1, 1, 1)

# box plot的第一个参数是数据，因为我们要绘制多条数据，所以我们必须将每条数据放入一个列表中。
axes1.boxplot(
    x=[tips.loc[tips['sex'] == 'Female', 'tip'],
       tips.loc[tips['sex'] == 'Male', 'tip']],
    labels=['Female', 'Male']
)

# x y 标签 和 标题。
axes1.set_xlabel('Sex')
axes1.set_ylabel('Tip')
axes1.set_title('Boxplot of Tips by Gender')

plt.show()
