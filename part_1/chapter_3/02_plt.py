#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
Matplotlib 基础知识。

@Time: 2023/6/10
@Author: Lingchen
@Prescription: P121.
"""
import logging
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

anscombe = sns.load_dataset('anscombe', data_home='../../data/seaborn-data', cache=True)
print(anscombe)

# 创建一个数据子集，只选取 dataset 列值是'I'的数据。
dataset_1 = anscombe[anscombe['dataset'] == 'I']

plt.plot(dataset_1['x'], dataset_1['y'])
plt.show()

# 默认 plot 是画线，若想画点，则可传参 'o'。
plt.plot(dataset_1['x'], dataset_1['y'], 'o')
plt.show()

