#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - Series 运用函数。

@Time: 2023/6/18
@Author: Lingchen
@Prescription: P255.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df = pd.DataFrame({
    'a': [10, 20, 30],
    'b': [20, 30, 40]
})
print(df)

# 对列进行平方计算。
print(df['a'] ** 2)

# 获取 'a' 列的类型。
print(type(df['a']))

print(type(df.iloc[0]))

# 该系列有一个名为 .apply() 的方法。
# 要使用 .apply() 方法，我们给它一个要在该系列中的每个元素中使用的函数。


def my_sq(x):
    """
    计算一个值的平方。
    :param x: 值。
    :return: 平方值
    """
    return x ** 2


# 在 'a' 列上应用平方函数。
sq = df['a'].apply(my_sq)
print(sq)


def my_exp(x, e):
    """
    计算指数的值。
    :param x: 值x。
    :param e: 指数e。
    :return: 计算值。
    """
    return x ** e


cubed = my_exp(2, 3)
print(cubed)

# TypeError: my_exp() missing 1 required positional argument: 'e'
# my_exp(2)

# 如果想在的系列中应用该函数，我们需要传入第二个参数。
# 为此，将第二个自变量作为关键字自变量传入 .apply() 。
ex = df['a'].apply(my_exp, e=2)
print(ex)

ex = df['a'].apply(my_exp, e=3)
print(ex)
