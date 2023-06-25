#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - filter 过滤器。

@Time: 2023/6/25
@Author: Lingchen
@Prescription: P335.
"""
import logging
import seaborn as sns

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())
print(tips.shape)

# 查看表大小的频率计数。
print(tips['size'].value_counts())

# 输出显示，表大小为1、5和6的情况并不常见。
# 根据您的需要，可能需要筛选出这些数据点。
# 在本例中，我们希望每组由30个或更多的观测值组成。
tips_filtered = (
    tips.groupby('size').filter(lambda x: x['size'].count() >= 30)
)
print(tips_filtered)
print(tips_filtered.shape)

print(tips_filtered['size'].value_counts())
