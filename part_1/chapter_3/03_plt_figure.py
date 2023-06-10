#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
绘子图，添加数据。
指定最终图形的尺寸，并放入较小的绘图以适应指定的尺寸。
这样，您可以在单个图形中显示结果。

@Time: 2023/6/10
@Author: Lingchen
@Prescription: P124.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

anscombe = sns.load_dataset('anscombe', data_home='../../data/seaborn-data', cache=True)
print(anscombe)

# 选取数据集。
dataset_1 = anscombe[anscombe['dataset'] == 'I']
dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']

fig = plt.figure()

# 告诉图应该如何布局。
# 我们将2行绘图，每行将有2个绘图。
axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)

# 为上面创建的每个轴添加一个绘图。
axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')

# 设置子标题。
axes1.set_title('dataset_1')
axes2.set_title('dataset_2')
axes3.set_title('dataset_3')
axes4.set_title('dataset_4')

# 设置整个标题。
fig.suptitle('Anscombe Data')

# 使用紧凑的布局，这样细节和标题就不会重叠。
fig.set_tight_layout(True)

plt.show()
