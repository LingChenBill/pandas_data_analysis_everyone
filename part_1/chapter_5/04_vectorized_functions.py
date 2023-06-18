#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 量化的函数。

@Time: 2023/6/18
@Author: Lingchen
@Prescription: P264.
"""
import logging
import pandas as pd
import numpy as np
import numba

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.DataFrame(
    {
        'a': [10, 20, 30],
        'b': [20, 30, 40]
    }
)
print(df)

# 可以利用 .vectorize() 函数和 decorator 对任何函数进行矢量化。
# 对代码进行矢量化也可以提高性能。


def avg_2(x, y):
    """
    计算平均值。
    :param x: 值x。
    :param y: 值y。
    :return: 平均值。
    """
    return (x + y) / 2


print(avg_2(df['a'], df['b']))

# 让更改函数并执行不可向量化的计算。


def avg_2_mod(x, y):
    """
    计算平均值，除了x是20。
    如果值为20，则返回一个缺失的值。
    :param x:
    :param y:
    :return:
    """
    if x == 20:
        return np.NAN
    else:
        return (x + y) / 2


# ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
# print(avg_2_mod(df['a'], df['b']))

# 如果给它一个单独的数字，而不是一个向量，它就会按预期工作。
print(avg_2_mod(10, 20))
print(avg_2_mod(20, 30))

# 利用 Numpy 向量化。
avg_2_mod_vect = np.vectorize(avg_2_mod)
print(avg_2_mod_vect(df['a'], df['b']))


@np.vectorize
def v_avg_2_mod(x, y):
    """
    可以使用Python装饰器来自动向量化函数，而无需创建新函数。
    装饰器是一个将另一个函数作为输入并修改该函数输出行为的函数。
    :param x: 值x。
    :param y: 值y。
    :return: 平均值。
    """
    if x == 20:
        return np.NAN
    else:
        return (x + y) / 2


# 可以直接使用矢量化函数, 而不必创建新功能。
print(v_avg_2_mod(df['a'], df['b']))


@numba.vectorize
def v_avg_2_numba(x, y):
    """
    numba library 旨在优化Python代码，尤其是对执行数学计算的数组的计算。
    就像numpy一样，它也有一个矢量化装饰器。
    :param x:
    :param y:
    :return:
    """
    if int(x) == 20:
        return np.NAN
    else:
        return (x + y) / 2


# ValueError: Cannot determine Numba type of <class 'pandas.core.series.Series'>
# print(v_avg_2_numba(df['a'], df['b']))

# 传入 numpy 数组。
print(v_avg_2_numba(df['a'].values, df['b'].values))
