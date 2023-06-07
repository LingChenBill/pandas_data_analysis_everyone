#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
df 的向量计算（传播）。

@Time: 2023/6/7
@Author: Lingchen
@Prescription: P94.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')
print(scientists)

first_half = scientists[:4]
second_half = scientists[4:]

print(first_half)

print(second_half)

# 整体 * 2 (字符串 * 2)
print(scientists * 2)
