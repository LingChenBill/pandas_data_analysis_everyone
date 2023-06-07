#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
通过 bool 来选取 df 的子集。

@Time: 2023/6/7
@Author: Lingchen
@Prescription: P93.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')

# 布尔向量将对行进行子集设置。
print(scientists['Age'].mean())

print(scientists.loc[scientists['Age'] > scientists['Age'].mean()])
