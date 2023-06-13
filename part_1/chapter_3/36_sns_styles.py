#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - 绘制 多个 样式的图形。

@Time: 2023/6/13
@Author: Lingchen
@Prescription: P187.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

seaborn_styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']

fig = plt.figure()

for idx, style in enumerate(seaborn_styles):
    plot_position = idx + 1
    with sns.axes_style(style):
        ax = fig.add_subplot(2, 3, plot_position)
        violin = sns.violinplot(
            data=tips, x='time', y='total_bill', ax=ax
        )
        violin.set_title(style)

fig.set_tight_layout(True)
plt.show()
