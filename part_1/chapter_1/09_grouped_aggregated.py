#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
分组和聚合计算.

@Time: 2023/6/4
@Author: Lingchen
@Prescription: P67.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', sep='\t')
print(df.head())

# 在我们的数据中，每年的平均预期寿命是多少?
# 1. 将我们的数据按年份分解
# 2. 获取“lifeExp”列
# 3 计算平均值
print(df.groupby('year')['lifeExp'].mean())

grouped_year_df = df.groupby('year')
print(type(grouped_year_df))
print(grouped_year_df)

grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print(type(grouped_year_df_lifeExp))
print(grouped_year_df_lifeExp)

mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)

# 反斜杠 允许我们分解1长行 python 代码分成多行
multi_group_var = df\
    .groupby(['year', 'continent'])\
    [['lifeExp', 'gdpPercap']]\
    .mean()
print(multi_group_var)

# 我们还可以包装整个语句 围绕圆括号
# 每一行都有.method（）
# 这是编写“方法链接”的首选样式
multi_group_parentheses = (
    df
    .groupby(['year', 'continent'])
    [['lifeExp', 'gdpPercap']]
    .mean()
)

print(multi_group_parentheses)

# 将 column 扁平化。
# 如果需要 "展平" DataFrame，可以使用.reset_index() 方法。
flat = multi_group_parentheses.reset_index()
print(flat)
