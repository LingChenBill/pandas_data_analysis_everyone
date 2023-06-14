#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 固定一列。

@Time: 2023/6/14
@Author: Lingchen
@Prescription: P202.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

pew = pd.read_csv('../../data/pew.csv')
print(pew.columns)

# 仅显示前几列。
print(pew.iloc[:, 0:5])

# #我们不需要指定 value_vars，因为我们想要透视, 除 "religion" 栏外的所有栏。
pew_long = pew.melt(id_vars='religion')
print(pew_long)

# melt method。
pew_long = pew.melt(id_vars='religion')
print(pew_long)

# melt function。
pew_long = pd.melt(pew, id_vars='religion')
print(pew_long)

pew_long = pew.melt(
    id_vars='religion', var_name='income', value_name='count'
)
print(pew_long)
