#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 丢失的值。

@Time: 2023/6/27
@Author: Lingchen
@Prescription: P356.
"""
import logging
from numpy import NAN, NaN, nan
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# NaN 不等于0或空字符串。这被称为"三值逻辑"。
print(NaN == True)

print(NaN == 0)

print(NaN == '')

print(NaN == NaN)

print(NaN == NAN)

print(NaN == nan)

print(nan == NAN)

# 测试是否丢失的值。
print(pd.isnull(NaN))

print(pd.isnull(nan))

print(pd.isnull(NAN))

# 测试非空值。
print(pd.notnull(NaN))

print(pd.notnull(42))

print(pd.notnull('missing'))
