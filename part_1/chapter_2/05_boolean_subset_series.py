#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
如何计算向量的基本描述性度量.
手动提供布尔向量以对我们的数据进行子集设置。

@Time: 2023/6/6
@Author: Lingchen
@Prescription: P84.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')
print(scientists.head())

ages = scientists['Age']
print(ages)

# 获取基本的统计数据。
print(ages.describe())

print(ages.mean())

# 如果我们想通过识别那些高于平均值的人来划分我们的年龄？
print(ages[ages > ages.mean()])

print(ages > ages.mean())

# 获取 dtype 为 bool 的系列。
print(type(ages > ages.mean()))

# 手动要获取 index 的布尔值。
# 手动提供布尔向量以对我们的数据进行子集设置。
manual_bool_values = [
    True,   # 0
    True,   # 1
    False,  # 2
    False,  # 3
    True,   # 4
    True,   # 5
    False,  # 6
    True,   # 7
]

print(ages[manual_bool_values])
