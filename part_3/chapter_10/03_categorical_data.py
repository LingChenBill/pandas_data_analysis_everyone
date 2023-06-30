#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 分类类型的数据。

@Time: 2023/6/30
@Author: Lingchen
@Prescription: P388.
"""
import logging
import seaborn as sns

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data/', cache=True)
print(tips.head())
print(tips.dtypes)

# pandas 有一个分类数据类型，可以对分类值进行编码。
# (1) 以这种方式存储数据可以提高内存和速度效率，尤其是当数据集包含许多重复的字符串值时。
# (2) 当一列值有顺序时（例如，Likert量表），分类数据可能是合适的。
# (3) 一些Python库了解如何处理分类数据。

# 首先将 sex 列转换为字符串对象。
tips['sex'] = tips['sex'].astype('str')
print(tips.info())

# 将 sex 列转换回分类数据。
tips['sex'] = tips['sex'].astype('category')
print(tips.info())
