#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 定制自己的函数。

@Time: 2023/6/23
@Author: Lingchen
@Prescription: P322.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.read_csv('../../data/gapminder.tsv', sep='\t')
print(df.head())


def my_mean(values):
    """
    定制 平均值 函数。
    :param values: 值。
    :return: 平均值。
    """
    n = len(values)

    sum_values = 0
    for value in values:
        sum_values += value

    return sum_values / n


# 在agg中使用我们的自定义函数。
agg_my_mean = df.groupby('year')['lifeExp'].agg(my_mean)
print(agg_my_mean)


def my_mean_diff(values, diff_value):
    """
    计算全球平均预期寿命 diff_value，并将其从每个分组值中减去。
    :param values: 值。
    :param diff_value: 平均预期寿命。
    :return: 平均值。
    """
    n = len(values)
    sum_values = 0

    for value in values:
        sum_values += value

    mean_value = sum_values / n
    return mean_value - diff_value


# 计算全球平均预期寿命。
global_mean = df['lifeExp'].mean()
print(global_mean)

# 具有多个参数的自定义聚合函数。
agg_mean_diff = (
    df.groupby('year')['lifeExp'].agg(my_mean_diff, diff_value=global_mean)
)

print(agg_mean_diff)
