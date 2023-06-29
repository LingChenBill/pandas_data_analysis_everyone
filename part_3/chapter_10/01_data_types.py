#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 数据类型。

@Time: 2023/6/29
@Author: Lingchen
@Prescription: P.
"""
import logging
import seaborn as sns

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 要获得存储在数据帧每列中的数据类型列表，调用 dtypes 属性。
print(tips.dtypes)

# int64 和 float64 类型分别表示不带小数点和带小数点的数值。
# category 数据类型代表分类变量。
# 它不同于存储任意 Python 对象（通常是字符串）的通用对象数据类型。
