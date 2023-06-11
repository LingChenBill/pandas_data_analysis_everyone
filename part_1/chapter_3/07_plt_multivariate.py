#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
复数量的数据绘图-散点图。

@Time: 2023/6/11
@Author: Lingchen
@Prescription: P136.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)

# 定制颜色。
colors = {
    'Female': '#f1a340',
    'Male': '#998ec3'
}

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)

# 绘制散点图。
axes1.scatter(
    data=tips,
    x='total_bill',
    y='tip',
    s=tips['size'] ** 2 * 10,     # 根据聚会规模设置圆点大小我们把数值乘以10，使点数变大并强调差异。
    c=tips['sex'].map(colors),    # 设置颜色。
    alpha=0.5                     # 设置透明度。
)

# 标签。
axes1.set_title('Colored by Sex and Sized by size')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')

# 最上面的标题。
scatter_plot.suptitle('Total Bill vs Tip')

plt.show()
