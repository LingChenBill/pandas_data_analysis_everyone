#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - lambda 函数使用。

@Time: 2023/6/18
@Author: Lingchen
@Prescription: P169.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.DataFrame(
    {
        'a': [10, 20, 30],
        'b': [20, 30, 40]
    }
)
print(df)


def my_sq(x):
    """
    计算平方值。
    :param x: 值x。
    :return: 平方值。
    """
    return x ** 2


df['a_sq'] = df['a'].apply(my_sq)
print(df)

# 使用 lambda。
df['a_sq_lamb'] = df['a'].apply(lambda x: x ** 2)
print(df)
