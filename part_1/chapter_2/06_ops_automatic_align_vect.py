#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
操作自动对齐和矢量化（广播）。

@Time: 2023/6/6
@Author: Lingchen
@Prescription: P88.
"""
import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')

ages = scientists['Age']
print(ages)

# 如果在两个长度相同的矢量之间执行运算，得到的矢量将是矢量的逐元素计算。
print(ages + ages)

print(ages * ages)

# 使用标量对向量执行操作，标量将在向量中的所有元素中循环使用。
print(ages + 100)

print(ages * 2)

# Pandas 中的广播指的是如何在不同形状的数组之间计算运算。
print(ages + pd.Series([1, 100]))

# ValueError: operands could not be broadcast together with shapes (8,) (2,) 。
print(ages + np.array([1, 100]))
