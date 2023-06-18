#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - df 运用函数。

@Time: 2023/6/18
@Author: Lingchen
@Prescription: P259.
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

# 当在数据帧上应用函数时，我们首先需要指定在哪个轴上应用函数。例如，逐列或逐行。


def print_me(x):
    """
    打印值。
    :param x: 值x。
    :return: 打印值。
    """
    print(x)


# 以列方式处理函数时，请在 .apply() 中使用axis=0参数（默认值）
df.apply(print_me, axis=0)

print(df['a'])
print(df['b'])


def avg_3(x, y, z):
    """
    计算3个值的平均均。
    :param x: 值x。
    :param y: 值y。
    :param z: 值z。
    :return: 平均值。
    """
    return (x + y + z) / 3


# TypeError: avg_3() missing 2 required positional arguments: 'y' and 'z'
# print(df.apply(avg_3))


def avg_3_apply(col):
    """
    计算 df 中的平均值。
    avg_3 函数但应用兼容通过将所有值作为第一个参数并解析出函数中的值。
    :param col: 列。
    :return: 平均值。
    """
    x = col[0]
    y = col[1]
    z = col[2]
    return (x + y + z) / 3


print(df.apply(avg_3_apply))

# 按行操作。
# IndexError: index 2 is out of bounds for axis 0 with size 2
# print(df.apply(avg_3_apply, axis=1))


def avg_2_apply(row):
    """
    按行计算平均值。
    :param row: 行。
    :return: 平均值。
    """
    x = row[0]
    y = row[1]
    return (x + y) / 2


print(df.apply(avg_2_apply, axis=1))
