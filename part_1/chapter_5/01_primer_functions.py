#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
定义，调用函数。

@Time: 2023/6/18
@Author: Lingchen
@Prescription: P253.
"""
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)


def my_sq(x):
    """
    计算一个值的平方。
    :param x: 值。
    :return: 平方值
    """
    return x ** 2


def avg_2(x, y):
    """
    计算两个值的平均值。
    :param x: 值x。
    :param y: 值y。
    :return: 平均值。
    """
    return (x + y) / 2


my_calc_1 = my_sq(4)
logging.info(my_calc_1)

my_calc_2 = avg_2(10, 20)
logging.info(my_calc_2)
