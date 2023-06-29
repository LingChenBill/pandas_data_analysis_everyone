#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 类型转换。

@Time: 2023/6/29
@Author: Lingchen
@Prescription: P381.
"""
import logging
import seaborn as sns
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())
print(tips.dtypes)

# 存储在列中的数据类型将决定可以对该列中找到的数据执行哪些类型的函数和计算。
# 要将值转换为字符串，我们在列上使用 .astype() 方法。

# 将类别 sex 列转换为字符串 dtype。
tips['sex_str'] = tips['sex'].astype(str)
print(tips.head())

# Python 有内置的 str、float、int、complex 和 bool 类型。
# 但是，也可以从 numpy 库中指定任何 dtype。
# 如果现在查看dtypes，您会发现 sex_str 现在有一个对象的 dtype。
print(tips.dtypes)

# 可以向 .astype() 方法提供任何内置或 numpy 类型来转换列的dtype。
# 将 total_bill 转换为字符串。
tips['total_bill'] = tips['total_bill'].astype(str)
print(tips.dtypes)

# 将其转换回浮点。
tips['total_bill'] = tips['total_bill'].astype(float)
print(tips.dtypes)

# 将变量转换为数值（例如int、float）时，
# 还可以使用Pandas to_numeric() 函数，它可以更好地处理非数值。

# 获取部分数据。
tips_sub_miss = tips.head(10).copy()
print(tips_sub_miss)

# 分配一些"丢失"的值。
tips_sub_miss.loc[[1, 3, 5, 7], 'total_bill'] = 'missing'
print(tips_sub_miss)

print(tips_sub_miss.dtypes)

# ValueError: could not convert string to float: 'missing'
# tips_sub_miss['total_bill'].astype(float)

# ValueError: Unable to parse string "missing" at position 1
# pd.to_numeric(tips_sub_miss['total_bill'])

# 从文档中看，如果将错误传递给'忽略'值，则我们的列中不会有任何更改。
tips_sub_miss['total_bill'] = pd.to_numeric(
    tips_sub_miss['total_bill'],
    errors='ignore'
)
print(tips_sub_miss)
print(tips_sub_miss.dtypes)

# 相反，如果传入'coerce'值，我们将获得'丢失'字符串的 NaN 值。
tips_sub_miss['total_bill'] = pd.to_numeric(
    tips_sub_miss['total_bill'],
    errors='coerce'
)
print(tips_sub_miss)
print(tips_sub_miss.dtypes)
