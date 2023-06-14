#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
sns - plot 上下文。

@Time: 2023/6/14
@Author: Lingchen
@Prescription: P188.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# seaborn库提供了一组上下文，可以根据不同的"上下文"快速调整图形的各个部分（文本大小、线宽、轴刻度大小等）。
contexts = pd.DataFrame(
    {
        'paper': sns.plotting_context('paper'),
        'notebook': sns.plotting_context('notebook'),
        'talk': sns.plotting_context('talk'),
        'poster': sns.plotting_context('poster'),
    }
)

print(contexts)

context_styles = contexts.columns

fig = plt.figure()
for idx, context in enumerate(context_styles):
    plot_position = idx + 1
    with sns.plotting_context(context):
        ax = fig.add_subplot(2, 2, plot_position)
        violin = sns.violinplot(
            data=tips, x='time', y='total_bill', ax=ax
        )
        violin.set_title(context)

fig.set_tight_layout(True)
plt.show()
